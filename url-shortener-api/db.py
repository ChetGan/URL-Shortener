from dotenv import load_dotenv
import pymongo
import os
import logging

#connecting to mongo database
def connect_mongo():
    load_dotenv()

    MONGO_HOST = os.getenv('MONGO_HOST')
    MONGO_PORT = os.getenv('MONGO_PORT')
    MONGO_DB = os.getenv('MONGO_DB')
    MONGO_USER = os.getenv('MONGO_USER')
    MONGO_PASS = os.getenv('MONGO_PASS')

    uri = "mongodb://{}:{}@{}:{}/{}?authSource=admin".format(MONGO_USER, MONGO_PASS, MONGO_HOST, MONGO_PORT, MONGO_DB)

    logging.info(uri)


    client = pymongo.MongoClient(uri, serverSelectionTimeoutMS=5000)
    return client.get_database(MONGO_DB)

