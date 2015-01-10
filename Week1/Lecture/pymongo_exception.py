import sys
import pymongo

connection = pymongo.MongoClient("mongodb://localhost")

db = connection.test
users = db.users

doc = {'firstname':'Todd', 'lastname':'Doughty'}
print doc
print "about to insert the document"

try:
    users.insert(doc)
except:
    print "insert failed:", sys.exc_info()[0]

print doc

doc = {'firstname':'Todd', 'lastname':'Doughty'}
print "inserting again"

try:
    users.insert(doc)
except:
    print " Second insert failed:", sys.exc_info()[0]

print doc

