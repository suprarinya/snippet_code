import mysql.connector
import pymongo

db_host = "127.0.0.1"
db_name = "endo5-1"

mysqldb = mysql.connector.connect(
    host = db_host,
    database = db_name,
    user="root",
    password=""
)
 
mycursor = mysqldb.cursor(dictionary=True)
mycursor.execute("SELECT * from autotext;")
myresult = mycursor.fetchall()

print(myresult)
print(len(myresult))

# mongodb_host = "mongodb://localhost:27017/"
 
# mongodb_dbname = "TestDump"
 
# myclient = pymongo.MongoClient(mongodb_host)
 
# mydb = myclient[mongodb_dbname]
 
# mycol = mydb["test_accessory"]
 
# if len(myresult) > 0:
 
#        x = mycol.insert_many(myresult) #myresult comes from mysql cursor
 
#        print(len(x.inserted_ids))
 
# print(myresult)

# mongodb_host = f"mongodb://127.0.0.1:27017/"
# mongodb_dbname = 'TestDump'

# myclient = pymongo.MongoClient(mongodb_host)
# mydb = myclient[mongodb_dbname]

# # find collection names
# collection_names = []
# collections = mydb.list_collection_names()
# for collection in collections:
#     collection_names.append(collection)
#     print(collection)

# print(len(collection_names))

