from selenium import webdriver

driver = webdriver.Chrome('chromedriver.exe')
#driver.maximize_window()
driver.get("https://www.facebook.com")
elem = driver.find_element_by_name("email")
elem.send_keys("");
elem = driver.find_element_by_name("pass")
elem.send_keys("");
elem.submit();
driver.get('https://www.facebook.com/search/people/?q=SBI&epa=SERP_TAB')
'''
img = driver.find_elements_by_xpath("//a[@class='search-result__result-link ember-view']")
for i in img:
    print(i.get_attribute("href"))
#x=driver.find_elements_by_xpath("//div[@class='item-inner']/span[1]");
#print(x);
'''

while True:
    l=0
    
    img = driver.find_elements_by_xpath("//a[@class='_32mo']")
    for i in img:
        print(i,' ',i.get_attribute("href"))
    #elem[-1].click()
    #driver.send_keys(keys.SPACE).perform()
    #footer = driver.find_element_by_tag_name("footer")
    '''for _ in range(8):
        driver.execute_script("arguments[0].scrollIntoView();", footer)
        time.sleep(1)
'''



'''
elem = driver.find_element_by_name("q")
elem.send_keys("state bank of india");
elem.submit();
#driver.findElementByClassName("_4jq5").click();
driver.get('https://www.facebook.com/search/people/?q=state%20bank%20of%20india&epa=SERP_TAB')
#driver.close()
'''
