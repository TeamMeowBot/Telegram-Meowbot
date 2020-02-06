from settings import parser
from telethon import TelegramClient
from telethon.sessions import StringSession

# Conversion functions
def str2bool(s):
    return s.lower() in ["true"]

# Global variables
API_KEY = parser.getint("API", "api_key")
API_HASH = parser.get("API", "api_hash")
SESSION = parser.get("API", "session_id")

VERBOSE = str2bool(parser.get("DEBUG", "verbose"))

cat = TelegramClient(StringSession(SESSION), API_KEY, API_HASH)

with open("modules.order") as f:
    MODULES = [line.rstrip() for line in f]
