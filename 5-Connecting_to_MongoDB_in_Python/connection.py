import os
from dotenv import load_dotenv
from pymongo import MongoClient


load_dotenv()
MONGO_URI = os.environ["MONGO_URI"]

client = MongoClient(MONGO_URI)


for db_name in client.list_database_names():
    print(db_name)

client.close()