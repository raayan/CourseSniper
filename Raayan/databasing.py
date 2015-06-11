__author__ = 'horsetamer'


import pymongo

from pymongo import MongoClient
client = MongoClient()


db = client.test1
posts = db.posts

var = raw_input("Enter 1 for CRN, or 2 for CNum, or 3 to print all: ")

if var == '1':
    var = raw_input("Please enter CRN: ")
    print(posts.find_one({"CRN": var}))


if var == '2':
    var1 = raw_input("Please enter Subject (the 'MTH' in MTH 101): ")
    var2 = raw_input("Please enter Class Number (the '101' in MTH 101): ")
    for post in posts.find({"CNum": var1 + " " + var2}):
        print(post)

if var == '3':
    for post in posts.find():
        print(post)