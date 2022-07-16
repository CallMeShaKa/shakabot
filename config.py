import os

from os import getenv
from dotenv import load_dotenv

load_dotenv()
API_ID = int(os.getenv("API_ID", "6"))
API_HASH = os.getenv("API_HASH", "eb06d4abfb49dc3eeb1aeb98ae0f581e")
BOT_USERNAME = os.getenv("BOT_USERNAME", "VcVideoRobot")
SUPPORT_GROUP = os.getenv("SUPPORT_GROUP", "DeeCodeSupport")
UPDATES_CHANNEL = os.getenv("UPDATES_CHANNEL", "DeeCodeBots")
SOURCE_CODE = os.getenv("SOURCE_CODE", "github.com/Sammy-XD/VcVideoPlayer")
BOT_TOKEN = list(map(int, getenv("BOT_TOKEN").split()))
