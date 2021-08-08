from pymongo import MongoClient

from mongoengine import connect
from mongoengine import Document, ListField, StringField, URLField



with MongoClient("mongodb://192.168.0.248:27017") as cliente:
    db = cliente.localbitcoin
    p2pSellers = db.p2pSellers

    print(p2pSellers.find_one({"username":"Crispin236"}))

    # find all
    for seller in p2pSellers.find():
        print(seller)


with connect(db="localbitcoin", host="192.168.0.248", port=27017) as conexion:
