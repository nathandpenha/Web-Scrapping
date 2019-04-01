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

#for i in range(0,10):
    #elem = driver.find_element_by_class_name("eyXLr wUAXj ")

    #elem.send_keys(Keys.PAGE_DOWN)

name="SBI"+".csv"
#t.strftime('%m-%d=%Y')+
with open(name, 'w') as f:
    f.write("Srno,Post Link,Likes"+"\n");
    


f.close()
body =driver.find_element_by_css_selector('body')
body.send_keys(Keys.PAGE_DOWN)
body.send_keys(Keys.PAGE_DOWN)
body.send_keys(Keys.PAGE_DOWN)
body.send_keys(Keys.PAGE_DOWN)
body.send_keys(Keys.PAGE_DOWN)
body.send_keys(Keys.PAGE_DOWN)
body.send_keys(Keys.PAGE_DOWN)
body.send_keys(Keys.PAGE_DOWN)
body.send_keys(Keys.PAGE_DOWN)

    
img = driver.find_elements_by_xpath("//div[@class='v1Nh3 kIKUG  _bz0w']")
ind=0    

for i in range(0,len(img)):
    inner=driver.find_elements_by_xpath("//div[@class='v1Nh3 kIKUG  _bz0w']")

    

    inner[ind].click()
    driver.get(driver.current_url)
    #print(i.get_attribute("href"))
    try:
        elem=driver.find_element_by_class_name("zV_Nj")
    except:
        elem=driver.find_element_by_class_name("vcOH2")
    print(elem.text)
    with open(name, 'a') as f:
        text=str((i+1))+","+driver.current_url+","+elem.text.replace(',','')+"\n"
        f.write(text);
    f.close()

    driver.get('https://www.instagram.com/theofficialsbi/')
    ind=ind+1
    #print(len(elem))
    #elem[-1].click()


