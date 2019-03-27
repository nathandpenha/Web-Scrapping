import time
import os
import random
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

if os.name == "posix":
	driver = webdriver.Chrome(executable_path="/Users/akasharora/PycharmProjects/Web-Scrapping/chromedriver")
else:
	driver = webdriver.Chrome('chromedriver.exe')

driver.get("file:///Users/akasharora/Sites/te/Gainful%20-%20Profile.html")

table = driver.find_element_by_xpath("//*[@id='ingTableBody']")


for td in driver.find_elements_by_xpath("//*[@id='ingTableBody']/tr/td"):
	if td.text != "":
		print(td.text, end="\t")
	else:
		print("\n")

print("*"*199)
