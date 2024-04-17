# pip install mysql-connector 
# pip install pymongo
import mysql.connector
import pymongo
import datetime
import sys

# arguments
# ------------------------------------------------- #
arg1 = sys.argv[1] 
arg2 = sys.argv[2]
arg3 = sys.argv[3]
arg4 = sys.argv[4]

# mysql
# ------------------------------------------------- #
# db_host = "127.0.0.1"
# db_name = "endo5-1"

db_host = arg1
db_name = arg2

mydb = mysql.connector.connect(
    host = db_host,
    database = db_name,
    user="root",
    password=""
)

mycursor = mydb.cursor(dictionary=True)
mycursor.execute("Show tables;")
all_tables = mycursor.fetchall()
 
#  get table name
tables_name = []
tables_data = []
for x in all_tables:
    table_name = x['Tables_in_'+db_name]
    tables_name.append(table_name)

    mycursor = mydb.cursor(dictionary=True)
    mycursor.execute(f"SELECT * from {table_name};")
    all_data = mycursor.fetchall()
    sub = []
    if len(all_data) != 0:
        for y in all_data:
            for key, value in y.items():
                if type(value) is datetime.date:
                    dt = datetime.datetime.combine(value, datetime.time.min)
                    y[key] = dt
            sub.append(y)
    # else: 
    #     field_names = [i[0] for i in mycursor.description ]
    #     y = {}
    #     for field in field_names:
    #         y[field] = None
    #     sub.append(y)
        
    tables_data.append(sub)

# mongodb
# ------------------------------------------------- #
# mongodb_host = "mongodb://localhost:27017/"
# mongodb_dbname = "TestDump"
mongodb_host = f"mongodb://{arg3}:27017/"
mongodb_dbname = arg4

myclient = pymongo.MongoClient(mongodb_host)
mydb = myclient[mongodb_dbname]

# find collection names
collection_names = []
collections = mydb.list_collection_names()
for collection in collections:
    collection_names.append(collection)

if len(tables_name) > 0 and len(tables_data) > 0:
    num_range = range(0, len(tables_name))
    for num in num_range:
        # print(num, len(tables_name))
        collection = mydb[tables_name[num]]

        if tables_name[num] in collection_names:
            collection.drop()
        
        if len(tables_data[num]) > 0:
            x = collection.insert_many(tables_data[num])
        else:
            mydb.create_collection(tables_name[num])
        


print('success')
        




