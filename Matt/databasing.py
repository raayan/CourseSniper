__author__ = 'horsetamer'


import pymongo

from pymongo import MongoClient
client = MongoClient()
db = client.test1
posts = db.posts

while True:
    var = raw_input("Enter 1 for CRN, or 2 for CNum, 3 to print all, or 4 to wipe database (-1 to end session): ")
    try:
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


        if var == '4':
            var1 = raw_input("Are you sure you would like to wipe the DB (Y/N?): ")
            if var1 == "Y" or var1 == "y":
                db.posts.remove({})
                print("All Posts in the 'posts' collection were wiped!")

        if var == '-1':
            quit(0)
    except:
        print("Connection Timeout")
