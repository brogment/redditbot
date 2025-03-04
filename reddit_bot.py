import praw
import os
from dotenv import load_dotenv
load_dotenv()


username = os.getenv("username")
password = os.getenv("password")
client_id = os.getenv("client_id")
client_secret = os.getenv("client_secret")