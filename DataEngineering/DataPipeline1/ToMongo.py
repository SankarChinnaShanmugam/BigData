import wikipedia
import wikipediaapi
import pymongo
from pymongo import MongoClient

wiki_wiki = wikipediaapi.Wikipedia('en')
# def print_categorymembers(categorymembers, level=0, max_level=1):
#         for c in categorymembers.values():
#             print("%s: %s (ns: %d)" % ("*" * (level + 1), c.title, c.ns))
#             if c.ns == wikipediaapi.Namespace.CATEGORY and level < max_level:
#                 print_categorymembers(c.categorymembers, level=level + 1, max_level=max_level)


cat = wiki_wiki.page("Category:Chemistry")
print("Category members: Category:Physics")
# print_categorymembers(cat.categorymembers)

client = MongoClient()
client = MongoClient('localhost', 27017)
client = MongoClient('mongodb://localhost:27017')
db = client.pymongo_test
db = client['pymongo_test']
posts = db.posts
post_data = {
    'title': 'Python and MongoDB',
    'content': 'PyMongo is fun, you guys',
    'author': 'Scott'
}
result = posts.insert_one(post_data)
print('One post: {0}'.format(result.inserted_id))

bills_post = posts.find_one({'author': 'Scott'})
print(bills_post)
