from os import getenv

from dotenv import load_dotenv

load_dotenv()
que = {}

TOKEN_BOT = getenv("TOKEN_BOT", "")
API_ID = getenv("API_ID", "")
API_HASH = getenv("API_HASH", "")
USER_ROOT = getenv("USER_ROOT", "")
SESSION_STRING = getenv("SESSION_STRING", "")