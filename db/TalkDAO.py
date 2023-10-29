from pymongo import MongoClient


def conn_mongodb():
    DB_ID = ""
    DB_PW = ""
    client = MongoClient(f"mongodb+srv://{DB_ID}:{DB_PW}@talkcluster.0efiswy.mongodb.net/")
    db = client["talk"]
    collection = db.get_collection("sarangbang")
    return collection


def add_talk(data):
    collection = conn_mongodb()
    collection.insert_one(data)