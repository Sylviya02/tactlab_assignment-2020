import requests
from bs4 import BeautifulSoup
import pymongo
from pymongo import MongoClient
import json

cluster=MongoClient("mongodb+srv://sylvi:sopi2102@cluster0.c1chg.mongodb.net/Countries?retryWrites=true&w=majority")
db=cluster["Countries"]
collection1=db["USA"]
collection2=db["UK"]
collection3=db["India"]
collection4=db["Canada"]
#result=collection.find({})
'''for key in result:
    print(key, ' : ', result[key])
    #values=key.values()
[print(key, value) for key, value in result.items()]
for x in result:
	#print(x)
	values = x.values()
	y=[]
	for k in x.values():
		#i=i+1
		y.append(k)
y=y[1:len(y)]
for i in y:
    print(i)'''
print("\nTOP 10 WORDS OF THE DECADE IN:\n")
print("1.USA\n2.UK\n3.India\n4.Canada\n")
a=1
while(a==1):
    choice=int(input("\nEnter Your choice:\n"))
    if (choice==1):
        result=collection1.find({})
    if (choice==2):
        result=collection2.find({})
    if (choice==3):
        result=collection3.find({})
    if (choice==4):
        result=collection4.find({})

    for x in result:
            #print(x)
            values = x.values()
            y=[]
            for k in x.values():
                    #i=i+1
                    y.append(k)
    y=y[1:len(y)]
    for i in y:
        print(i)
    a=int(input("\nDo you want to continue:Yes(1)/No(0):\n"))

    


    
