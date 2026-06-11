# Diablo 4 Build Agent 🎮

An AI-powered Discord bot that helps you create and optimize Diablo 4 builds. Uses a hardcoded knowledge base with optional LLM enhancement for intelligent recommendations.

## Features

- 🎯 **Build Suggestions** - Get complete builds for any class and playstyle
- ⚙️ **Gear Recommendations** - Find optimal gear combinations
- 📊 **Build Analysis** - Analyze your current character setup
- 🤖 **AI Enhancement** - Optional GPT-4/Claude integration for advanced insights
- 💬 **Discord Integration** - Run directly in your Discord server

## Requirements

- Python 3.9+
- Discord.py
- python-dotenv
- openai (optional, for LLM features)

## Setup

### 1. Clone & Install Dependencies

```bash
git clone https://github.com/moodyshadow/diablo4-build-agent.git
cd diablo4-build-agent
pip install -r requirements.txt
```

### 2. Configure Environment

Copy `.env.example` to `.env` and fill in:

```env
DISCORD_TOKEN=your_discord_bot_token
OPENAI_API_KEY=your_openai_api_key  # Optional
```

### 3. Create Discord Bot

1. Go to [Discord Developer Portal](https://discord.com/developers/applications)
2. Click "New Application"
3. Go to "Bot" tab and click "Add Bot"
4. Copy the token to `.env`
5. Under "OAuth2" > "URL Generator", select:
   - Scopes: `bot`
   - Permissions: `Send Messages`, `Read Messages`, `Embed Links`
6. Use the generated URL to invite bot to your server

### 4. Run the Bot

```bash
python bot.py
```

## Commands

- `/build <class> <playstyle>` - Get a build recommendation
- `/analyze <class>` - Analyze current gear setup
- `/compare <build1> <build2>` - Compare two builds
- `/suggest-gear <class>` - Get gear recommendations
- `/help` - Show all commands

## Architecture

```
diablo4-build-agent/
├── bot.py                 # Main Discord bot
├── config.py              # Configuration
├── knowledge_base.py      # Hardcoded D4 data
├── llm_integration.py     # LLM enhancement (optional)
├── commands/              # Discord commands
├── requirements.txt       # Dependencies
├── .env.example          # Environment template
└── README.md
```

## Build Database

The knowledge base includes:
- All 5 Diablo 4 classes with unique builds
- Legendary items and unique gear
- Skill rotations and synergies
- Leveling guides per class

## Optional: LLM Integration

To enable AI-powered insights:

1. Get an API key from [OpenAI](https://platform.openai.com) or [Anthropic](https://www.anthropic.com)
2. Add to `.env`: `OPENAI_API_KEY=sk-...`
3. The bot will automatically use LLM for complex queries

## Contributing

Feel free to improve builds, add new strategies, or enhance the bot!

## License

MIT

## Support

Need help? Create an issue or DM the bot `/help`

---

**Happy building, Nephalem!** ⚔️