from prettytable import PrettyTable
import pymongo
x = PrettyTable()
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["WikiDBDetails"]
mycol = mydb["WikiDBDetails"]

myresults = list(mycol.find().limit(10))
x.field_names = ["Category Name", "URL", " Summary"]
for record in myresults:
	summary = str(record['Summary'])
	x.add_row([record['CategoryName'], record['URL'], summary[:50]])


print(x)