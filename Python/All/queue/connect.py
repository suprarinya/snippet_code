# package need connect mongodb
# py -m pip install pymongo
from pymongo import MongoClient


def connect_db(host, port, collection):
    client = MongoClient(host, port, serverSelectionTimeoutMS=5000, connectTimeoutMS=5000)
    db     = client[collection]
    return db, client

def connect_table(db, table):
    table = db[table]
    return table

def get_one(table, where):
    data = table.find_one(where)
    return data

def insert_one(table, insert):
    lastest_id = table.insert_one(insert).inserted_id
    return lastest_id

def close_connection(client):
    client.close()


