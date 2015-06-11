__author__ = 'horsetamer'

import pymongo
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from time import sleep
from bs4 import BeautifulSoup
from pymongo import MongoClient

import re

#scans a web page and returns list of tuples CRN, Course Name, Status
def page_scan(html):
    list = []
    soup = BeautifulSoup(html)
    # print(soup.prettify())
    j = 1
    add = "01"
    while (soup.find(id = "rpResults_ctl" + add + "_lblTitle") != None):
        CRN = soup.find(id = "rpResults_ctl" + add + "_lblCRN").string.strip()
        CNum = soup.find(id = "rpResults_ctl" + add + "_lblCNum").string.strip()
        Status = soup.find(id = "rpResults_ctl" + add + "_lblStatus").string.strip()
        obj = (CRN, CNum, Status)
        print(obj)
        list.append(obj)
        if j < 10:
            add = "0" + str(j)
        else:
            add = str(j)
        j+=2;
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
        page_scan(driver.page_source)
        sleep(2)
        selectDept = Select(driver.find_element_by_name('ddlDept'))
        selectDept.select_by_index(i)
        sleep(1)
        submit = driver.find_element_by_name("btnSearchTop").click()
        driver.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
        sleep(2)
        page_scan(driver.page_source)

def crawlpage(page):
    driver = webdriver.PhantomJS()
    driver.get("https://cdcs.ur.rochester.edu/")
    driver.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
    sleep(2)
    selectTerm = Select(driver.find_element_by_name('ddlTerm'))
    selectTerm.select_by_index(1)
    selectDept = Select(driver.find_element_by_name('ddlDept'))
    options = selectDept.options

    populateDB(driver.page_source)
    sleep(2)
    selectDept = Select(driver.find_element_by_name('ddlDept'))
    selectDept.select_by_index(page)
    sleep(1)
    submit = driver.find_element_by_name("btnSearchTop").click()
    driver.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
    sleep(2)
    populateDB(driver.page_source)

def populateDB(html):
    soup = BeautifulSoup(html)
    # print(soup.prettify())
    j = 1
    add = "01"
    while (soup.find(id = "rpResults_ctl" + add + "_lblTitle") != None):
        CRN = soup.find(id = "rpResults_ctl" + add + "_lblCRN").string.strip()
        CNum = soup.find(id = "rpResults_ctl" + add + "_lblCNum").string.strip()
        Status = soup.find(id = "rpResults_ctl" + add + "_lblStatus").string.strip()
        obj = (CRN, CNum, Status)
        addToDB(CRN, CNum, Status)
        print(obj)

        j+=2;

        if j < 10:
            add = "0" + str(j)
        else:
            add = str(j)

def addToDB(CRN, CNum, Status):
        client = MongoClient()
        db = client.test1
        post = {"CNum": CNum, "CRN": CRN, "Status": Status}
        posts = db.posts
        post_id = posts.insert_one(post).inserted_id



#Begin Process
# web_crawler()

crawlpage(1)