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

#scans webpage and pulls courses and stores in tuple (CRN, NAME, STATUS)
def page_scan(html):
    list = []
    soup = BeautifulSoup(html)
    # print(soup.prettify())
    j = 1
    add = "01"
    while (soup.find(id = "rpResults_ctl" + add + "_lblTitle") != None):
        print(add)
        CRN = soup.find(id = "rpResults_ctl" + add + "_lblCRN").string.strip()
        CNum = soup.find(id = "rpResults_ctl" + add + "_lblCNum").string.strip()
        Status = soup.find(id = "rpResults_ctl" + add + "_lblStatus").string.strip()
        print(CRN + " || " + CNum + " || " + Status)
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
        page_scan(driver.page_source)
        sleep(2)
        selectDept = Select(driver.find_element_by_name('ddlDept'))
        selectDept.select_by_index(i)
        sleep(1)
        submit = driver.find_element_by_name("btnSearchTop").click()
        driver.execute_script("return document.getElementsByTagName('html')[0].innerHTML")





#
# driver = webdriver.Firefox()
# driver.get("https://cdcs.ur.rochester.edu/")
# sleep(2)
#
# selectYear = Select(driver.find_element_by_name("ddlTerm"))
# selectYear.select_by_index(6)
# sleep(1)
#
# selectSchool = Select(driver.find_element_by_name("ddlSchool"))
# selectSchool.select_by_index(6)
#
# sleep(1)
# selectDept = Select(driver.find_element_by_name("ddlDept"))
# selectDept.select_by_index(1)
#
# sleep(1)
#
# submit = driver.find_element_by_name("btnSearchTop").click()
#
# driver.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
# sleep(2)
# html = driver.page_source
#
# page_scan(html)
#
web_crawler()