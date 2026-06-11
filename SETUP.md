# Setup Guide - Diablo 4 Build Agent

## Step-by-Step Setup

### 1. Create Discord Bot

1. Go to [Discord Developer Portal](https://discord.com/developers/applications)
2. Click "New Application" and name it "D4 Build Agent"
3. Go to the "Bot" tab
4. Click "Add Bot"
5. Copy the TOKEN (you'll need this for `.env`)
6. Disable "Public Bot" if you want it private
7. Go to "OAuth2" → "URL Generator"
8. Select Scopes:
   - `bot`
9. Select Permissions:
   - `Send Messages`
   - `Read Messages/View Channels`
   - `Embed Links`
   - `Read Message History`
10. Copy the generated URL and open it to invite the bot to your server

### 2. Clone Repository

```bash
git clone https://github.com/moodyshadow/diablo4-build-agent.git
cd diablo4-build-agent
```

### 3. Set Up Python Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure Environment Variables

```bash
# Copy the template
cp .env.example .env

# Edit .env with your text editor
```

Fill in `.env`:
```env
DISCORD_TOKEN=your_bot_token_here
OPENAI_API_KEY=sk-... # Optional! Only if you want LLM features
BOT_PREFIX=!
DEBUG_MODE=False
```

### 6. Run the Bot

```bash
python bot.py
```

You should see:
```
✅ Bot logged in as D4 Build Agent#1234
📊 Connected to X guild(s)
```

### 7. Test in Discord

In any Discord channel where the bot is present, try:
```
!build barbarian damage
!buildlist sorceress
!search tornado
!help
```

---

## Optional: Enable LLM Features

If you want AI-powered insights:

1. Get API key:
   - **OpenAI**: https://platform.openai.com/account/api-keys
   - **Claude**: https://console.anthropic.com/

2. Add to `.env`:
   ```env
   OPENAI_API_KEY=sk-your-key-here
   ```

3. Restart bot - LLM features will now be available

---

## Troubleshooting

### Bot doesn't start
- Check `.env` has valid `DISCORD_TOKEN`
- Ensure Python 3.9+ is installed
- Run `pip install -r requirements.txt` again

### Bot doesn't respond
- Make sure bot has "Send Messages" permission in the channel
- Check the channel isn't in a category with restricted permissions
- Verify bot is online in Discord

### LLM not working
- Ensure `OPENAI_API_KEY` is valid
- Check account has credits available
- Look for error messages in console

---

## File Structure

```
diablo4-build-agent/
├── bot.py              # Main bot file
├── config.py           # Settings & configuration
├── knowledge_base.py   # D4 build database
├── llm_integration.py  # Optional AI enhancement
├── requirements.txt    # Python dependencies
├── .env.example        # Template for environment variables
├── .gitignore          # Git ignore rules
├── README.md           # Main documentation
└── SETUP.md            # This file
```

---

## Next Steps

1. **Customize builds** - Edit `knowledge_base.py` to add your own strategies
2. **Add commands** - Check `bot.py` and add new commands
3. **Improve LLM** - Tweak prompts in `llm_integration.py`
4. **Deploy** - Host on a service like Heroku, Replit, or your own server

Happy building! ⚔️