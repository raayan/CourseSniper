__author__ = 'Matt'


#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'mlee'
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from time import sleep
from bs4 import BeautifulSoup
import re


driver = webdriver.Firefox()
driver.get("https://cdcs.ur.rochester.edu/")
driver.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
sleep(2)

selectYear = Select(driver.find_element_by_name("ddlTerm"))
selectYear.select_by_index(1)
sleep(1)

selectSchool = Select(driver.find_element_by_name("ddlSchool"))
selectSchool.select_by_index(1)

sleep(1)
selectDept = Select(driver.find_element_by_name("ddlDept"))
selectDept.select_by_index(3)

sleep(1)


submit = driver.find_element_by_name("btnSearchTop").click()

driver.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
sleep(2)
html = driver.page_source




sleep(2)
print(html)