import wikipediaapi
import wikipedia
import requests
import re
from bs4 import BeautifulSoup

lst_Value = []
def print_categorymembers(categorymembers, level=0, max_level=1):
        for c in categorymembers.values():
            lst_Value.append("%s " % (c.title))
            if c.ns == wikipediaapi.Namespace.CATEGORY and level < max_level:
                print_categorymembers(c.categorymembers, level=level + 1, max_level=max_level)



wiki_wiki = wikipediaapi.Wikipedia('en')
cat = wiki_wiki.page("Category:Physics")
print_categorymembers(cat.categorymembers)


for e in lst_Value:
	#data = {'str': e}
	print("Category Name : ", e)
	print(wikipedia.page(e).url)
	print(wikipedia.page(e).references)
	print(wikipedia.page(e).title)
	print(wikipedia.page(e).categories)
	print(wikipedia.page(e).links)
	print(wikipedia.page(e).summary[0:60])


# print(cat.url)
# print(cat.references)
# print(cat.title)
# print(cat.categories)
# print(cat.links)

print(wikipedia.page("Python").url)
print(wikipedia.page("Python").references)
print(wikipedia.page("Python").title)
print(wikipedia.page("Python").categories)
print(wikipedia.page("Ubuntu").links)