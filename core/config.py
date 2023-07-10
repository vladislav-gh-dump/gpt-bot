import os
from dotenv import load_dotenv


load_dotenv()

CONFIG = {
    'BOT_TOKEN': os.getenv("BOT_TOKEN"),
    'OPENAI_API_KEY': os.getenv("OPENAI_API_KEY"),
    'ADMIN_ID': os.getenv("ADMIN_ID")
}
