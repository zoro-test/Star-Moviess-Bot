from os import getenv
from dotenv import load_dotenv

load_dotenv()

API_ID_1 = int(getenv("API_ID_1", "11973721"))
API_HASH_1 = getenv("API_HASH_1", "5264bf4663e9159565603522f58d3c18")

BOT_TOKEN_1 = getenv("BOT_TOKEN_1", "5865794282:AAEOwU2-vXMXOsi8KymZ-T46cGe03MeQZQ0")
OWNER_ID = int(getenv("OWNER_ID", "1391556668"))

