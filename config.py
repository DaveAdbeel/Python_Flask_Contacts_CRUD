import os

from dotenv import load_dotenv

load_dotenv()

user = os.getenv("MYSQL_USER")
passwd = os.getenv("MYSQL_PASSWORD")
host = os.getenv("MYSQL_HOST")
db = os.getenv("MYSQL_DATABASE")

SECRET_KEY = os.getenv("SECRET_KEY")
DATABASE_CONNECTION_URI = f'mysql://{user}:{passwd}@{host}/{db}'
