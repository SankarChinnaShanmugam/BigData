from kafka import KafkaConsumer
from pymongo import MongoClient
from json import loads
import wikipedia
import wikipediaapi

message = ''
url = ''
summary = ''
references = ''
links = ''
subCategories = ''

#Connecting the kafka Consumer
consumer = KafkaConsumer(
    'WikiDBDetails', bootstrap_servers=['127.0.0.1:9092'], auto_offset_reset='earliest', enable_auto_commit=True,
     group_id='my-group', value_deserializer=lambda x: loads(x.decode('utf-8')))

client = MongoClient('localhost:27017')
collection = client.WikiDBDetails.WikiDBDetails
wiki_wiki = wikipediaapi.Wikipedia('en')

#Process the consumer listner data.
for message in consumer:
	print("Started the Consumer to process the data.")
	message = message.value
	print("CategoryName: ", message)
	page_py = wiki_wiki.page(message)
	try:
		if page_py.exists():
			url = str(wikipedia.page(message).url)
			print("URL: ", url)
			#region Fetech Additonal Parameters
			summary = str(wikipedia.page(message).summary[0:200])
			print("Summary: ", summary)

			if page_py.categories == '':
				pass
			else:
				references = str(page_py.categories)
				print("References: ", references)

			if page_py.links == '':
				pass
			else:
				links = str(page_py.links)
				print("Links: ", links)

			subCategories = str(wikipedia.page(message).categories[0])
			print("SubCategories: ", subCategories)
			#endregion
			print('\n')
			print('\n')
			print(" Completed the Consumer record along with additional parameters.")
			print('\n')
			print('Inserting into each and every record into the Mongo DB.')
			result = collection.insert(
				{"CategoryName": message, "URL": url, "Summary": summary, "References": references, "Links": links,
				 "SubCategories": subCategories})
	except:
		pass