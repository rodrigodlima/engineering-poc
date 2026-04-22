import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv() 

env = os.getent("ENV")


DB_URLS = [
    ("DEV", "db.dev.local"),
    ("HML", "db.hml.local"),
]


def get_db_url(db_url: str) -> str:
    return next(environement for name, environement in DB_URLS 
                if name == db_url)


db_url = get_db_url(env)

client = MongoClient(db_url)

