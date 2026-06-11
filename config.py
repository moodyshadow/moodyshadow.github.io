"""
Configuration settings for Diablo 4 Build Agent
"""

import os
from dotenv import load_dotenv

load_dotenv()

# Discord Bot Configuration
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
BOT_PREFIX = os.getenv("BOT_PREFIX", "!")
DEBUG_MODE = os.getenv("DEBUG_MODE", "False").lower() == "true"

# LLM Configuration (Optional)
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", None)
USE_LLM = OPENAI_API_KEY is not None

# Bot Settings
BOT_NAME = "D4 Build Agent"
BOT_VERSION = "1.0.0"

# Diablo 4 Classes
CLASSES = [
    "barbarian",
    "sorceress",
    "necromancer",
    "druid",
    "rogue"
]

# Playstyles
PLAYSTYLES = [
    "damage",
    "tank",
    "support",
    "hybrid",
    "leveling"
]

# Error Messages
ERRORS = {
    "invalid_class": "❌ Invalid class. Choose from: {}",
    "invalid_playstyle": "❌ Invalid playstyle. Choose from: {}",
    "not_configured": "⚠️ Bot not properly configured. Check your .env file.",
    "api_error": "⚠️ API error occurred. Please try again later.",
}

# Success Messages
SUCCESS = {
    "build_found": "✅ Build found!",
    "analysis_complete": "✅ Analysis complete!",
}