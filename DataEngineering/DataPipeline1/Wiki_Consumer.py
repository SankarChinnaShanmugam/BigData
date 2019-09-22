from kafka import KafkaConsumer
from pymongo import MongoClient
from json import loads
from Wiki import Wiki

consumer = KafkaConsumer(
    'wikidata',
     bootstrap_servers=['127.0.0.1:9092'],
     auto_offset_reset='earliest',
     enable_auto_commit=True,
     group_id='my-group',
     value_deserializer=lambda x: loads(x.decode('utf-8')))

client = MongoClient('localhost:27017')
collection = client.wikidata.wikidata

total_docs =0
for message in consumer:
    message = message.value
    result = collection.insert_one(message)
    # print('{} added to {}'.format(message, collection))
    print("inserted Value: ", message, "\n\n")
    total_docs = total_docs + 1

print("Total number of records: ", total_docs)





client = MongoClient('localhost:27017')
collection = client.wikidata.wikidata

# create a new list for the insert_many() method call
mongo_docs = []

# iterate over the list of fruits
for message in consumer:
    # create a new MongoDB document dict
    doc={}
    # message = message.value
    doc['Name'] = 'Category'

    doc['Value'] = message

    mongo_docs += [doc]
    print("total inserted:", len(mongo_docs))

# make an API request to MongoDB to insert_many() fruits
result = collection.insert_many(mongo_docs)

# get the total numbers of docs inserted
total_docs = len(result.inserted_ids)

print("total inserted:", total_docs)
print("inserted IDs:", result.inserted_ids, "\n\n")

