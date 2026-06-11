"""
Diablo 4 Build Agent - Discord Bot
Main bot file with command handlers
"""

import discord
from discord.ext import commands
from config import DISCORD_TOKEN, BOT_PREFIX, DEBUG_MODE, ERRORS, CLASSES, PLAYSTYLES
from knowledge_base import get_build, get_all_builds_for_class, search_builds
from llm_integration import enhance_build_recommendation, get_build_tips
import asyncio

# Bot Setup
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=BOT_PREFIX, intents=intents)

# ============== Events ==============

@bot.event
async def on_ready():
    print(f"✅ Bot logged in as {bot.user}")
    print(f"📊 Connected to {len(bot.guilds)} guild(s)")
    await bot.change_presence(activity=discord.Activity(
        type=discord.ActivityType.watching, 
        name="Diablo 4 builds | /help"
    ))


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send(f"❌ Command not found. Use `/help` for available commands.")
    else:
        await ctx.send(f"❌ Error: {str(error)}")
        if DEBUG_MODE:
            print(f"Error: {error}")


# ============== Commands ==============

@bot.hybrid_command(name="build", description="Get a Diablo 4 build recommendation")
async def get_build_command(ctx, class_name: str = None, playstyle: str = None):
    """Get a recommended build for a class and playstyle"""
    
    if not class_name or not playstyle:
        embed = discord.Embed(
            title="❌ Missing Parameters",
            description=f"Usage: `{BOT_PREFIX}build <class> <playstyle>`",
            color=discord.Color.red()
        )
        embed.add_field(
            name="Available Classes",
            value=", ".join(CLASSES),
            inline=False
        )
        embed.add_field(
            name="Available Playstyles",
            value=", ".join(PLAYSTYLES),
            inline=False
        )
        await ctx.send(embed=embed)
        return
    
    # Validate inputs
    class_name = class_name.lower()
    playstyle = playstyle.lower()
    
    if class_name not in CLASSES:
        await ctx.send(ERRORS["invalid_class"].format(", ".join(CLASSES)))
        return
    
    if playstyle not in PLAYSTYLES:
        await ctx.send(ERRORS["invalid_playstyle"].format(", ".join(PLAYSTYLES)))
        return
    
    # Get build
    build = get_build(class_name, playstyle)
    
    if not build:
        await ctx.send(f"❌ No build found for {class_name} with {playstyle} playstyle.")
        return
    
    # Create embed
    embed = discord.Embed(
        title=f"⚔️ {build['name']}",
        description=build['description'],
        color=discord.Color.gold()
    )
    embed.add_field(name="Class", value=class_name.capitalize(), inline=True)
    embed.add_field(name="Playstyle", value=playstyle.capitalize(), inline=True)
    embed.add_field(name="Difficulty", value=build['difficulty'], inline=True)
    embed.add_field(name="Key Skills", value=", ".join(build['key_skills']), inline=False)
    embed.add_field(name="Legendary Items", value=", ".join(build['legendary_items']), inline=False)
    embed.add_field(name="Stats Priority", value=", ".join(build['stats_priority']), inline=False)
    
    # Pros/Cons
    pros_text = "✅ " + "\n✅ ".join(build['pros'])
    cons_text = "❌ " + "\n❌ ".join(build['cons'])
    
    embed.add_field(name="Pros", value=pros_text, inline=True)
    embed.add_field(name="Cons", value=cons_text, inline=True)
    embed.add_field(
        name="Budget Friendly",
        value="💰 Yes" if build['budget_friendly'] else "💸 No",
        inline=True
    )
    
    embed.set_footer(text="React with 🤖 for AI insights (if configured)")
    
    await ctx.send(embed=embed)


@bot.hybrid_command(name="buildlist", description="List all builds for a class")
async def list_builds(ctx, class_name: str = None):
    """Show all available builds for a class"""
    
    if not class_name:
        embed = discord.Embed(
            title="❌ Missing Parameter",
            description=f"Usage: `{BOT_PREFIX}buildlist <class>`",
            color=discord.Color.red()
        )
        embed.add_field(name="Available Classes", value=", ".join(CLASSES), inline=False)
        await ctx.send(embed=embed)
        return
    
    class_name = class_name.lower()
    
    if class_name not in CLASSES:
        await ctx.send(ERRORS["invalid_class"].format(", ".join(CLASSES)))
        return
    
    builds = get_all_builds_for_class(class_name)
    
    if not builds:
        await ctx.send(f"❌ No builds found for {class_name}.")
        return
    
    embed = discord.Embed(
        title=f"🎮 {class_name.capitalize()} Builds",
        color=discord.Color.blue()
    )
    
    for playstyle, build in builds.items():
        embed.add_field(
            name=f"{build['name']} ({playstyle})",
            value=build['description'],
            inline=False
        )
    
    embed.set_footer(text=f"Use {BOT_PREFIX}build {class_name} <playstyle> for more details")
    await ctx.send(embed=embed)


@bot.hybrid_command(name="search", description="Search builds by keyword")
async def search_builds_command(ctx, keyword: str = None):
    """Search for builds by name or keyword"""
    
    if not keyword:
        await ctx.send(f"Usage: `{BOT_PREFIX}search <keyword>`")
        return
    
    results = search_builds(keyword)
    
    if not results:
        await ctx.send(f"❌ No builds found matching '{keyword}'")
        return
    
    embed = discord.Embed(
        title=f"🔍 Search Results for '{keyword}'",
        color=discord.Color.purple()
    )
    
    for result in results[:10]:  # Limit to 10 results
        build = result["build"]
        embed.add_field(
            name=f"{build['name']} ({result['class']})",
            value=f"*{build['description']}*",
            inline=False
        )
    
    await ctx.send(embed=embed)


@bot.hybrid_command(name="help", description="Show help and available commands")
async def help_command(ctx):
    """Display help information"""
    
    embed = discord.Embed(
        title="🎮 Diablo 4 Build Agent Help",
        color=discord.Color.blurple()
    )
    
    embed.add_field(
        name=f"{BOT_PREFIX}build <class> <playstyle>",
        value="Get a specific build recommendation",
        inline=False
    )
    embed.add_field(
        name=f"{BOT_PREFIX}buildlist <class>",
        value="List all builds for a class",
        inline=False
    )
    embed.add_field(
        name=f"{BOT_PREFIX}search <keyword>",
        value="Search builds by keyword",
        inline=False
    )
    embed.add_field(
        name="Available Classes",
        value=", ".join([c.capitalize() for c in CLASSES]),
        inline=False
    )
    embed.add_field(
        name="Available Playstyles",
        value=", ".join([p.capitalize() for p in PLAYSTYLES]),
        inline=False
    )
    embed.add_field(
        name="Examples",
        value=(
            f"`{BOT_PREFIX}build barbarian damage`\n"
            f"`{BOT_PREFIX}buildlist sorceress`\n"
            f"`{BOT_PREFIX}search tornado`"
        ),
        inline=False
    )
    
    embed.set_footer(text="Enjoy building your character!")
    await ctx.send(embed=embed)


@bot.hybrid_command(name="ping", description="Check bot latency")
async def ping(ctx):
    """Check bot latency"""
    latency = round(bot.latency * 1000)
    await ctx.send(f"🏓 Pong! Latency: {latency}ms")


# ============== Main ==============

def main():
    if not DISCORD_TOKEN:
        print("❌ DISCORD_TOKEN not set in .env file!")
        return
    
    print("🚀 Starting Diablo 4 Build Agent...")
    print(f"📝 Prefix: {BOT_PREFIX}")
    print(f"🐛 Debug Mode: {DEBUG_MODE}")
    
    try:
        bot.run(DISCORD_TOKEN)
    except Exception as e:
        print(f"❌ Failed to start bot: {e}")


if __name__ == "__main__":
    main()