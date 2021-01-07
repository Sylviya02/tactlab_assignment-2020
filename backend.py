import pymongo
from pymongo import MongoClient
cluster = MongoClient("mongodb+srv://sylvi:sopi2102@cluster0.c1chg.mongodb.net/Countries?retryWrites=true&w=majority")
db=cluster["Countries"]
collections=db["USA"]
collections.insert_one({"_id":5,"One":"Anglosphere","Two":"Anti-suffragism",
       "Three":"Destigmatizing","Four":"Influencer",
       "Five":"Self-isolate","Six":"Social Distancing",
       "Seven":"Theonomous","Eight":"Unfamthomed",
       "Nine":"WFH","Ten":"Zoodle"})
collections=db["UK"]
post2={"One":"Brexit","Two":"Bumble",
       "Three":"Doughnuting","Four":"Eurostar",
       "Five":"Glamping","Six":"Ham",
       "Seven":"Hoodie","Eight":"Smeg",
       "Nine":"Twuncing","Ten":"Yogalates"}
collections.insert_one(post2)
collections=db["India"]
post3={"One":"Austerity","Two":"Existential",
       "Three":"Feminism","Four":"Geek",
       "Five":"Misinformation","Six":"Photobomb",
       "Seven":"Pragmatic","Eight":"Selfie",
       "Nine":"Socialism","Ten":"Surreal"}
collections.insert_one(post3)
collections=db["Canada"]
post4={"One":"Athleisure","Two":"Black spider memo",
       "Three":"Croggie","Four":"Gold fishing",
       "Five":"Hashtag","Six":"Mansplain",
       "Seven":"Microaggression","Eight":"Sandwich generation",
       "Nine":"Trout pout","Ten":"Vancouver Olympics"}
collections.insert_one(post4)

