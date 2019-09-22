import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["WikiDBDetails"]
mycol = mydb["WikiDBDetails"]

myresults = list(mycol.find().limit(20))
objects = []
performance = []
for record in myresults:
     count = 0
     res = record['References']
     val = res.split('),')
     for i in val:
          count += 1

     objects.append(record['CategoryName'])
     performance.append(count)
     print('Category Name:  {} - Number of References: {}'.format(record['CategoryName'], count))

y_pos = np.arange(len(objects))


plt.barh(y_pos, performance, align='center', alpha=0.5)
plt.yticks(y_pos, objects)
plt.xlabel('References')
plt.title('List of Categories Vs No. of References')

plt.show()