import pymongo
import json
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["WikiDBDetails"]
mycol = mydb["WikiDBDetails"]

# for x in mycol.find():
#     print(x)

# for x in mycol.find({"References": {'$regex' : ".*Biology.*"}}):
#     print(x['CategoryName'])
# for doc in mycol.find().limit(2).sort([
#         ('URL', pymongo.ASCENDING),
#         ('References', pymongo.DESCENDING)]):
#     print(doc['CategoryName'])


# cursor = mycol.find().limit(10)
# for record in cursor:
#     print(record)

# cursor = mycol.find({"CategoryName": "Chemistry"})
#
# print(mycol.find_one({"CategoryName": {"$exists": False}}, sort=[("CategoryName", 1)])["CategoryName"])


# for passenger in mycol.find().limit(10):
# 	print('Category Name:  {} \n URL: {}'.format(passenger['CategoryName'], passenger['URL']))

# print('Number of Category: {:d} '.format(mycol.count_documents({})))

myresults = list(mycol.find().limit(10))
# for record in myresults:
# 	print(record)

# my_json_string = json.dumps(myresults)

# for record in myresults:
#      print(record)
#      print(record['_id'])
#      print('\n')
#      print(record['CategoryName'])
#      print('\n')
#      print(record['URL'])
#      print('\n')
#      print(record['Summary'])
#      print('\n')
#      print(record['References'])
#      print('\n')
#      print(record['SubCategories'])
# myresults = list(mycol.find().limit(10))
for record in myresults:
     count = 0
     res = record['References']
     val = res.split('),')
     for i in val:
          count += 1
     print('Category Name:  {} - Number of References: {}'.format(record['CategoryName'], count))

