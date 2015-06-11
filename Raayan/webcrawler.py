__author__ = 'horsetamer'

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from time import sleep
from bs4 import BeautifulSoup
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
        # print(CRN + " || " + CNum + " || " + Status)
        list.append((CRN, CNum, Status))
        if j < 10:
            add = "0" + str(j)
        else:
            add = str(j)
        j+=2;
    return list

driver = webdriver.Firefox()
driver.get("https://cdcs.ur.rochester.edu/")
driver.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
sleep(2)

#choose year
selectYear = Select(driver.find_element_by_name("ddlTerm"))
selectYear.select_by_index(1)
sleep(1)

#choose
selectDept = Select(driver.find_element_by_name("ddlDept"))
selectDept.select_by_index(3)
sleep(1)


submit = driver.find_element_by_name("btnSearchTop").click()

driver.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
sleep(2)
html = driver.page_source


print(page_scan(html))