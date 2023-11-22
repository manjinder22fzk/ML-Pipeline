import pymongo
import os


import certifi
ca = certifi.where()

class MongodbOperation:

    def __init__(self) -> None:

        from urllib.parse import quote_plus

        username = "manjinder_singh"
        password = "Engineering96@"

        escaped_username = quote_plus(username)
        escaped_password = quote_plus(password)

        # Use the escaped credentials in your MongoDB URI
        MONGO_DB_URL = f"mongodb+srv://{escaped_username}:{escaped_password}@cluster0.ftk5qa5.mongodb.net/?retryWrites=true&w=majority"
        # mongodb+srv://manjinder_singh:<password>@cluster0.ftk5qa5.mongodb.net/?retryWrites=true&w=majority

        # MONGO_DB_URL = 'mongodb+srv://manjindersinghfzk:Engineering96@@kafka-sensor.izsbegb.mongodb.net/?retryWrites=true&w=majority'
        self.client = pymongo.MongoClient(MONGO_DB_URL,tlsCAFile=ca)
        self.db_name="ineuron"

    def insert_many(self,collection_name,records:list):
        self.client[self.db_name][collection_name].insert_many(records)

    def insert(self,collection_name,record):
        self.client[self.db_name][collection_name].insert_one(record)
        
