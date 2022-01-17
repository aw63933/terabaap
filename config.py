import os

from dotenv import load_dotenv
from pyrogram import Client, filters
from pytgcalls import PyTgCalls

# For Local Deploy
if os.path.exists(".env"):
    load_dotenv(".env")

# Necessary Vars
API_ID = int(os.getenv("API_ID", "7342182"))
API_HASH = os.getenv("API_HASH", "a80ca7acb06d0cb64a967ba33ef1e536")
SESSION = os.getenv("SESSION", "BQATRWTiLK-utz3teRqq_WVfJdyGSx2tOFiC7WpnC_utFeY12qBjV8vv-OG75rs6VLgszjAcSrADQKeRNmgpkY3wH9pcLmJso8Vy37OZ1YapY0sUqNQMZaYg5wjwwAsMtPXZkqTHvQiAyDYbsv0zpTnp5Vd3vTTSt6bc9pPi1dEmHd30xHjJEYCiI9v_hlVpmI1_Cxh7knY75HTbkd62lqXmX-BQ6Bzzo2U6nkMM-j6UpvcAv8xM-pWPbIRWWkQquo7VK2Qoo1ICxmPKnovBdxCkXwKiHczmtbHfNR5zHZ4bLwqGvX8ml_MIzmGlR2YOCkamH5xQfioeFK8HQoULaDPqAAAAASyxYRsA")
HNDLR = os.getenv("HNDLR", "/")
SUDO_USERS = list(map(int, os.getenv("SUDO_USERS", "1362497646").split()))


contact_filter = filters.create(
    lambda _, __, message: (message.from_user and message.from_user.is_contact)
    or message.outgoing
)

bot = Client(SESSION, API_ID, API_HASH, plugins=dict(root="VcUserBot"))
call_py = PyTgCalls(bot)
