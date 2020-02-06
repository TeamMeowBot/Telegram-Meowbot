from telethon.sync import TelegramClient
from telethon.sessions import StringSession
from settings import parser, configwrite

API_KEY = parser.getint("API", "API_KEY")
API_HASH = parser.get("API", "API_HASH")

if parser.get("API", "SESSION_ID") == "":
    with TelegramClient(StringSession(), API_KEY, API_HASH) as client:
        parser.set("API", "SESSION_ID", client.session.save())
        configwrite()
else:
    print("""A session is already active, please clear SESSION_ID value on bot.config file\nand remove meowbot.session file.""")
    exit(1)