from time import sleep
from json import dumps
from kafka import KafkaProducer
import wikipediaapi

lst_Value = []
def print_categorymembers(categorymembers, level=0, max_level=1):
        for c in categorymembers.values():
            lst_Value.append("%s: %s (ns: %d)" % ("*" * (level + 1), c.title, c.ns))
            if c.ns == wikipediaapi.Namespace.CATEGORY and level < max_level:
                print_categorymembers(c.categorymembers, level=level + 1, max_level=max_level)


wiki_wiki = wikipediaapi.Wikipedia('en')
producer = KafkaProducer(bootstrap_servers=['127.0.0.1:9092'], value_serializer=lambda x: dumps(x).encode('utf-8'))
cat = wiki_wiki.page("Category:Chemistry")
print_categorymembers(cat.categorymembers)

for e in lst_Value:
	data = {'str': e}
	producer.send('wikidata', value=data)
	sleep(1)