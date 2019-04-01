from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import csv

import datetime
t = datetime.datetime.now()


driver = webdriver.Chrome('chromedriver.exe')
#driver.maximize_window()
driver.get("https://www.instagram.com/accounts/login/")
elem = driver.find_element_by_name("username")
elem.send_keys("");
elem = driver.find_element_by_name("password")
elem.send_keys("");
elem.submit();
driver.get('https://www.instagram.com/theofficialsbi/')
elem = driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
elem.send_keys("sbi");


name="SBI_Instagram"+".csv"
#t.strftime('%m-%d=%Y')+
with open(name, 'w') as f:
    f.write("Srno,Page"+"\n");
    

f.close()
img = driver.find_elements_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
ind=0    

for i in range(0,len(img)):
    elem = driver.find_elements_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
    

    print(elem[i].text)
    with open(name, 'a') as f:
        text=str((i+1))+","+elem.text+"\n"
        f.write(text);
    f.close()
