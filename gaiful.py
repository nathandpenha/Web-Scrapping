import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome('chromedriver.exe')
#driver.maximize_window()
driver.get("https://www.gainful.com/consultation/?gender=Male")
time.sleep(5)
elem=driver.find_element_by_id("question7choice1")

elem.submit()
driver.get("https://www.gainful.com/consultation/?gender=Male")
time.sleep(5)
elem=driver.find_element_by_id("dob-month")
elem.send_keys("04")
elem=driver.find_element_by_id("dob-day")
elem.send_keys("10")
elem=driver.find_element_by_id("dob-year")
elem.send_keys("1996")
time.sleep(2)
elem.send_keys(Keys.ENTER)
time.sleep(6)

en =  driver.find_element_by_xpath("//*[@id='question_form']/div[1]/input")
move = ActionChains(driver)
move.click_and_hold(en).move_by_offset(-180, 0).release().perform()

time.sleep(2)
en =  driver.find_element_by_xpath("//*[@id='question_form']/div[1]/section/input")
move = ActionChains(driver)
move.click_and_hold(en).move_by_offset(-180, 0).release().perform()
en.send_keys(Keys.ENTER)

time.sleep(5)

en =  driver.find_element_by_xpath("//*[@id='question_form']/div/input")
move = ActionChains(driver)
move.click_and_hold(en).move_by_offset(-180, 0).release().perform()



en =  driver.find_element_by_xpath("//*[@id='question_form']/div/section/input")
move = ActionChains(driver)
move.click_and_hold(en).move_by_offset(-180, 0).release().perform()

en =  driver.find_element_by_xpath("//*[@id='question_form']/section/input")
move = ActionChains(driver)
move.click_and_hold(en).move_by_offset(-180, 0).release().perform()
en.send_keys(Keys.ENTER)


time.sleep(5)

en =  driver.find_element_by_xpath('//*[@id="question8choice1"]')
en.click()
en.send_keys(Keys.ENTER)

time.sleep(5)


en =  driver.find_element_by_xpath("//*[@id='question9choice1']")
en.click()
en.send_keys(Keys.ENTER)

time.sleep(5)
en =  driver.find_element_by_xpath('//*[@id="question3choice2"]')
en.click()
en.send_keys(Keys.ENTER)


time.sleep(5)



en =  driver.find_element_by_xpath("//*[@id='question5choice1']")
en.click()
en.send_keys(Keys.ENTER)

time.sleep(5)


en =  driver.find_element_by_xpath("//*[@id='question10choice1']")
en.click()
en.send_keys(Keys.ENTER)

time.sleep(5)



en =  driver.find_element_by_xpath('//*[@id="question_form"]/div/input')
move = ActionChains(driver)
move.click_and_hold(en).move_by_offset(-180, 0).release().perform()
en.send_keys(Keys.ENTER)
time.sleep(5)


en =  driver.find_element_by_xpath("//*[@id='question81choice1']")
en.click()
en.send_keys(Keys.ENTER)

time.sleep(5)


en =  driver.find_element_by_xpath("//*[@id='question11choice1']")
en.click()
en.send_keys(Keys.ENTER)

time.sleep(5)


en =  driver.find_element_by_xpath("//*[@id='question12choice1']")
en.click()
en.send_keys(Keys.ENTER)

time.sleep(5)

en =  driver.find_element_by_xpath("//*[@id='question13choice1']")
en.click()
en.send_keys(Keys.ENTER)

time.sleep(5)

en =  driver.find_element_by_xpath('//*[@id="question_form"]/fieldset/div[1]/label')
en.click()
en.send_keys(Keys.ENTER)

time.sleep(5)

