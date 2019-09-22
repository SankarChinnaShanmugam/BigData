import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["wikidata"]
mycol = mydb["wikidata"]

for x in mycol.find():
    print(x)