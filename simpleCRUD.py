from pymongo import MongoClient

# client = MongoClient("localhost", 27017)
# client = MongoClient("mongodb://localhost:27017/")
client = MongoClient("mongodb://192.168.0.21:27017/")

db = client.bot
# db = client["bot"]


# operaciones = db.operacioens
operaciones = db["operaciones"]


for r in operaciones.find():
    print(r)
