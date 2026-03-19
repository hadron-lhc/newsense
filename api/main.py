from dotenv import load_dotenv
import os

load_dotenv()  # carga el .env

api_key = os.getenv("NEWSAPI_KEY")
