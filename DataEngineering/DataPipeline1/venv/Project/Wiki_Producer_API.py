from time import sleep
from json import dumps
from kafka import KafkaProducer
import wikipediaapi

lst_Value = []
def print_categorymembers(categorymembers, level=0, max_level=1):
        for c in categorymembers.values():
            lst_Value.append("%s " % (c.title))
            if c.ns == wikipediaapi.Namespace.CATEGORY and level < max_level:
                print_categorymembers(c.categorymembers, level=level + 1, max_level=max_level)

try:
	print(" Started into the Producer rogram.")

	#Setting the wiki page into english format.
	wiki_wiki = wikipediaapi.Wikipedia('en')

	#Connecting to the Kafka Server.
	producer = KafkaProducer(bootstrap_servers=['127.0.0.1:9092'], value_serializer=lambda x: dumps(x).encode('utf-8'))

	#Setting the Category Type, which is input to the wiki page
	cat = wiki_wiki.page("Category:Chemistry")

	#Fetch the required data from APIs.
	print_categorymembers(cat.categorymembers)

	for e in lst_Value:
		print("Sending the each and every record to consumer.\n", e)
		producer.send('WikiDBDetails', value=e)
		sleep(1)
except:
	print("There is Problem in Producer.")