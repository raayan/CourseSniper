__author__ = 'Matt'


#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'mlee'
import string
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from time import sleep
from bs4 import BeautifulSoup
import re
import pymongo
from pymongo import MongoClient
import smtplib
from email.mime.text import MIMEText


URI = "mongodb://admin:tightjeans@ds043982.mongolab.com:43982/ur_coursesniper"
client = MongoClient(URI)
cs_db = client.ur_coursesniper
class_list = cs_db.classes


#scans webpage and pulls courses and stores in tuple (CRN, NAME, STATUS)
def page_scan(html):
    list = []
    soup = BeautifulSoup(html)
    j = 1
    add = "01"
    while (soup.find(id = "rpResults_ctl" + add + "_lblTitle") != None):
        print(add)
        CRN = soup.find(id = "rpResults_ctl" + add + "_lblCRN").string.strip()
        CNum = soup.find(id = "rpResults_ctl" + add + "_lblCNum").string.strip()
        Status = soup.find(id = "rpResults_ctl" + add + "_lblStatus").string.strip()
        #print(CRN + " || " + CNum + " || " + Status)
        list.append((CRN, CNum, Status))
        j+=2;
        if j < 10:
            add = "0" + str(j)
        else:
            add = str(j)
    return list



#populates/updates database, webcrawls
def web_crawler():
    driver = webdriver.PhantomJS()
    driver.get("https://cdcs.ur.rochester.edu/")
    driver.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
    sleep(2)
    selectTerm = Select(driver.find_element_by_name('ddlTerm'))
    selectTerm.select_by_index(1)
    selectDept = Select(driver.find_element_by_name('ddlDept'))
    options = selectDept.options

    for i in range(1, len(options)):
        selectDept = Select(driver.find_element_by_name('ddlDept'))
        selectDept.select_by_index(i)
        sleep(3)
        submit = driver.find_element_by_name("btnSearchTop").click()
        driver.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
        sleep(3)
        classes = page_scan(driver.page_source)
        update_DB(classes)
        print(classes)
        sleep(3)

    driver.close()

def update_DB(class_tuples):
    global class_list

    posts = []
    for x in class_tuples:
        if(class_list.find_one({"CRN" : x[0] }) == None):
            posts.append({"CRN": x[0], "NAME": x[1], "STATUS": x[2], "Users": []})
        else:
            update_entry(x)

    if(posts):
        class_list.insert_many(posts)



def update_entry(class_tuple):
    global class_list

    post = class_list.find_one({"CRN": class_tuple[0]})

    #if(post['STATUS'] == 'closed' and class_tuple[2] == 'Open' ):
        #sendemail

    class_list.update_one({"CRN": class_tuple[0]}, {'$set': {'STATUS': class_tuple[2]}})

def start_sniping(email, crn):
    global class_list

    post = class_list.find_one({"CRN": crn})
    class_list.update_one({"CRN": crn}, {'$addToSet': {'Users': email}})
    send_confirm(email, post)

def snipe(crn):
    post = class_list.find_one({"CRN": crn})
    for email in post['Users']:
        send_snipemail(email, post)


def send_snipemail(email, post):
    crn = post['CRN']
    s_class = post['NAME']
    from_addr = 'ur.snipeteam@gmail.com'

    #add option to resnipe here, and link to registration page
    msg = MIMEText("Hey!\n\n The class " + s_class + " you are currently sniping has just opened up.\n\nSnag it while it's still available! \n\n GL,\n Your Faithful Snipers")
    msg['From'] = 'ur.snipeteam@gmail.com'
    msg['To'] =  email
    msg['Subject'] = "The course " + s_class + ' has just opened up. Snag it!'


    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(from_addr,'tightjeans')
    server.sendmail('ur.snipeteam', email, msg.as_string())
    server.quit()

def send_confirm(email, post):
    crn = post['CRN']
    s_class = post['NAME']

    from_addr = 'ur.snipeteam@gmail.com'

    #add option to resnipe here, and link to registration page
    msg = MIMEText("Hey!\n\n You have successfully started watching the class " + s_class + ".\n\n We will notify you if it becomes available! \n\n GL,\n Your Faithful Snipers")
    msg['From'] = 'ur.snipeteam@gmail.com'
    msg['To'] =  email
    msg['Subject'] = "You have successfully started sniping " + s_class + "."

    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(from_addr,'tightjeans')
    server.sendmail('ur.snipeteam', email, msg.as_string())
    server.quit()


#web_crawler()

#snipe('10013')
start_sniping('raayanp01@gmail.com', '10013')