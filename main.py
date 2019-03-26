import time
import os
import random
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

TIME = 7


def random_gender():
	options = ["Male", "Female"]
	return random.choice(options)


def random_name():
	alpha = []
	for x in range(97, 123):
		alpha.append(chr(x))
	
	name = ""
	
	for x in range(random.randint(5, 9)):
		name += random.choice(alpha)
	
	return name


def random_year():
	year = []
	for x in range(1920, 2000):
		year.append(x)
	
	return random.choice(year)


def random_date():
	date = []
	for x in range(1, 29):
		date.append(x)
	
	return random.choice(date)


def random_month():
	month = []
	for x in range(13):
		month.append(x)
	
	return random.choice(month)


def question_exercise():
	options = [1, 2, 3]
	# 1 => 1 or less
	# 2 => 2 - 3
	# 3 => 4 or more
	return str(random.choice(options))


def question_sports():
	options = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
	return str(random.choice(options))


def question_type_exercise():
	options = [1, 2, 3, 4, 5, 6, 7]
	# weightlifting, cardio, sports, yoga, dance, swimming, other
	return str(random.choice(options))


if os.name == "posix":
	driver = webdriver.Chrome(executable_path="/Users/akasharora/PycharmProjects/Web-Scrapping/chromedriver")
# driver.maximize_window()
# driver = webdriver.Safari(executable_path="/usr/bin/safaridriver")
# driver = webdriver.Firefox()
else:
	driver = webdriver.Chrome('chromedriver.exe')

driver.get("https://www.gainful.com/consultation/?gender="+random_gender())
time.sleep(TIME)
elem = driver.find_element_by_id("question7choice1")
elem.submit()
driver.get("https://www.gainful.com/consultation/?gender="+random_gender())
time.sleep(TIME)
elem = driver.find_element_by_id("dob-month")
elem.send_keys(random_month())
elem = driver.find_element_by_id("dob-day")
elem.send_keys(random_date())
elem = driver.find_element_by_id("dob-year")
elem.send_keys(random_year())
elem.send_keys(Keys.ENTER)
time.sleep(TIME)
elem.send_keys(Keys.ENTER)
time.sleep(TIME)

en = driver.find_element_by_xpath("//*[@id='question_form']/div[1]/input")
move = ActionChains(driver)
move.click_and_hold(en).move_by_offset(-180, 0).release().perform()

time.sleep(TIME)
en = driver.find_element_by_xpath("//*[@id='question_form']/div[1]/section/input")
move = ActionChains(driver)
move.click_and_hold(en).move_by_offset(-180, 0).release().perform()
en.send_keys(Keys.ENTER)

time.sleep(TIME)

en = driver.find_element_by_xpath("//*[@id='question_form']/div/input")
move = ActionChains(driver)
move.click_and_hold(en).move_by_offset(-180, 0).release().perform()

en = driver.find_element_by_xpath("//*[@id='question_form']/div/section/input")
move = ActionChains(driver)
move.click_and_hold(en).move_by_offset(-180, 0).release().perform()

en = driver.find_element_by_xpath("//*[@id='question_form']/section/input")
move = ActionChains(driver)
move.click_and_hold(en).move_by_offset(-180, 0).release().perform()
en.send_keys(Keys.ENTER)

time.sleep(TIME)

en = driver.find_element_by_xpath('//*[@id="question8choice' + question_exercise() + '"]')
en.click()
en.send_keys(Keys.ENTER)

time.sleep(TIME)

en = driver.find_element_by_xpath("//*[@id='question9choice" + question_type_exercise() + "']")
en.click()
en.send_keys(Keys.ENTER)

time.sleep(TIME)
en = driver.find_element_by_xpath('//*[@id="question3choice2"]')
en.click()
en.send_keys(Keys.ENTER)

# en = driver.find_element_by_xpath('//*[@id="question1choice' + question_sports() + '"]')
# en.click()
# en.send_keys(Keys.ENTER)


time.sleep(TIME)

en = driver.find_element_by_xpath("//*[@id='question5choice1']")
en.click()
en.send_keys(Keys.ENTER)

time.sleep(TIME)

en = driver.find_element_by_xpath("//*[@id='question10choice1']")
en.click()
en.send_keys(Keys.ENTER)

time.sleep(TIME)

en = driver.find_element_by_xpath('//*[@id="question_form"]/div/input')
move = ActionChains(driver)
move.click_and_hold(en).move_by_offset(-180, 0).release().perform()
en.send_keys(Keys.ENTER)
time.sleep(TIME)

en = driver.find_element_by_xpath("//*[@id='question81choice1']")
en.click()
en.send_keys(Keys.ENTER)

time.sleep(TIME)

en = driver.find_element_by_xpath("//*[@id='question11choice1']")
en.click()
en.send_keys(Keys.ENTER)

time.sleep(TIME)

en = driver.find_element_by_xpath("//*[@id='question12choice1']")
en.click()
en.send_keys(Keys.ENTER)

time.sleep(TIME)

en = driver.find_element_by_xpath("//*[@id='question14choice1']")
en.click()
en.send_keys(Keys.ENTER)

time.sleep(TIME)

# en = driver.find_element_by_xpath('//*[@id="question_form"]/fieldset/div[1]/label')
# en.click()
# en.send_keys(Keys.ENTER)

time.sleep(TIME)

en = driver.find_element_by_id("first_name")
en.send_keys(random_name())
en = driver.find_element_by_id("email-form")
en.send_keys(random_name(), "@", random_name(), '.com')
en.send_keys(Keys.ENTER)

time.sleep(TIME)


en = driver.find_element_by_xpath('//*[@id="ingTableBody"]/tr[1]/td[1]')
print(en.text);
en = driver.find_element_by_xpath('//*[@id="ingTableBody"]/tr[1]/td[2]')
print(en.text);
en = driver.find_element_by_xpath('//*[@id="ingTableBody"]/tr[2]/td[1]')
print(en.text);
en = driver.find_element_by_xpath('//*[@id="ingTableBody"]/tr[2]/td[2]')
print(en.text);
en = driver.find_element_by_xpath('//*[@id="ingTableBody"]/tr[3]/td[1]')
print(en.text);
en = driver.find_element_by_xpath('//*[@id="ingTableBody"]/tr[3]/td[2]')
print(en.text);
en = driver.find_element_by_xpath('//*[@id="ingTableBody"]/tr[4]/td[1]')
print(en.text);
en = driver.find_element_by_xpath('//*[@id="ingTableBody"]/tr[4]/td[2]')
print(en.text);
en = driver.find_element_by_xpath('//*[@id="ingTableBody"]/tr[5]/td[1]')
print(en.text);
en = driver.find_element_by_xpath('//*[@id="ingTableBody"]/tr[5]/td[2]')
print(en.text);
en = driver.find_element_by_xpath('//*[@id="ingTableBody"]/tr[6]/td[1]')
print(en.text);
en = driver.find_element_by_xpath('//*[@id="ingTableBody"]/tr[6]/td[2]')
print(en.text);
