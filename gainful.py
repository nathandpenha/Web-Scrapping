import time
import os
import random
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


def random_name():
	alpha = []
	for x in range(97, 123):
		alpha.append(chr(x))
	
	name = ""
	
	for x in range(random.randint(5, 9)):
		name += random.choice(alpha)
	
	return name


fileName = "output/VarWeightHeightAndOthers-SlimToMuscle-MALE.txt"
TIME = 8
PREFIX_TAB = "\t\t"
NEW_LINE = "\n"

# Open File
fileHandler = open(fileName, "a")

for increase_offset in [0, 80, 120, 160, 250]:
	if os.name == "posix":
		driver = webdriver.Chrome(executable_path="/Users/akasharora/PycharmProjects/Web-Scrapping/chromedriver")
	else:
		driver = webdriver.Chrome('chromedriver.exe')
	
	driver.maximize_window()
	
	fileHandler.write("***********************************************************************************" + NEW_LINE)
	# fileHandler.write("Test for Goal Body Type " + str() + NEW_LINE)
	fileHandler.write("\tInputs" + NEW_LINE)
	
	# Open Link
	gender = "Male"
	fileHandler.write(PREFIX_TAB + "Gender : " + gender + NEW_LINE)
	driver.get("https://www.gainful.com/consultation/?gender=" + gender)
	time.sleep(TIME)
	# Select Input -> Gender
	elem = driver.find_element_by_id("question7choice1")
	elem.submit()
	driver.get("https://www.gainful.com/consultation/?gender=" + gender)
	time.sleep(TIME)
	
	# DOB
	month = "01"
	day = "01"
	year = "1980"
	elem = driver.find_element_by_id("dob-month")
	elem.send_keys(month)
	elem = driver.find_element_by_id("dob-day")
	elem.send_keys(day)
	elem = driver.find_element_by_id("dob-year")
	elem.send_keys(year)
	fileHandler.write(PREFIX_TAB + "DOB : " + day + "/" + month + "/" + year + NEW_LINE)
	elem.send_keys(Keys.ENTER)
	time.sleep(TIME)
	elem.send_keys(Keys.ENTER)
	time.sleep(TIME)
	
	# Body Type
	en = driver.find_element_by_xpath("//*[@id='question_form']/div[1]/input")
	move = ActionChains(driver)
	move.click_and_hold(en).move_by_offset(-250, 0).release().perform()
	fileHandler.write(PREFIX_TAB + "Current Body Type : " + driver.find_element_by_xpath(
		"//*[@id='question_form']/div[1]/output").text + NEW_LINE)
	time.sleep(TIME)
	en = driver.find_element_by_xpath("//*[@id='question_form']/div[1]/section/input")
	move = ActionChains(driver)
	move.click_and_hold(en).move_by_offset(100, 0).release().perform()
	fileHandler.write(PREFIX_TAB + "Goal Body Type :" + driver.find_element_by_xpath(
		"//*[@id='question_form']/div[1]/section/output").text + NEW_LINE)
	en.send_keys(Keys.ENTER)
	time.sleep(TIME)
	
	# Physical Attributes -> Height / Current Weight / Goal Weight
	randomHeight = [increase_offset, -increase_offset]
	en = driver.find_element_by_xpath("//*[@id='question_form']/div/input")
	move = ActionChains(driver)
	move.click_and_hold(en).move_by_offset(random.choice(randomHeight), 0).release().perform()
	fileHandler.write(
		PREFIX_TAB + "Height : " + driver.find_element_by_xpath("//*[@id='question_form']/div/output").text + NEW_LINE)
	en = driver.find_element_by_xpath("//*[@id='question_form']/div/section/input")
	move = ActionChains(driver)
	move.click_and_hold(en).move_by_offset(-increase_offset, 0).release().perform()
	fileHandler.write(PREFIX_TAB + "Current Weight : " + driver.find_element_by_xpath(
		"//*[@id='question_form']/div/section/output").text + NEW_LINE)
	en = driver.find_element_by_xpath("//*[@id='question_form']/section/input")
	move = ActionChains(driver)
	move.click_and_hold(en).move_by_offset(increase_offset, 0).release().perform()
	fileHandler.write(PREFIX_TAB + "Goal Weight : " + driver.find_element_by_xpath(
		"//*[@id='question_form']/section/output").text + NEW_LINE)
	en.send_keys(Keys.ENTER)
	time.sleep(TIME)
	
	# Exercise -> Times a week
	exercise = random.choice([1, 2, 3])
	en = driver.find_element_by_xpath('//*[@id="question8choice' + str(exercise) + '"]')
	en.click()
	ex_text = "1 or Less" if exercise == 1 else "2-3" if exercise == 2 else "4 or more"
	fileHandler.write(PREFIX_TAB + "Exercise @ Times/Week : " + ex_text + NEW_LINE)
	en.send_keys(Keys.ENTER)
	time.sleep(TIME)
	
	# Type of Exercise
	type_ex = 7
	try:
		en = driver.find_element_by_xpath('//*[@id="question9choice' + str(type_ex) + '"]')
	except:
		driver.refresh()
		time.sleep(TIME)
		en = driver.find_element_by_xpath('//*[@id="question9choice' + str(type_ex) + '"]')
	options = {1: "weightlifting", 2: "Cardio", 3: "Sports", 4: "Yoga", 5: "Dance", 7: "Swimming", 8: "Others"}
	fileHandler.write(PREFIX_TAB + "Type of Exercise : " + options[type_ex] + NEW_LINE)
	en.click()
	en.send_keys(Keys.ENTER)
	time.sleep(TIME)
	
	# Why take Protein Powder
	protein = random.choice([2, 3, 4, 5, 6, 7, 8, 9])
	try:
		en = driver.find_element_by_xpath('//*[@id="question3choice' + str(protein) + '"]')
	except:
		driver.refresh()
		time.sleep(TIME)
		en = driver.find_element_by_xpath('//*[@id="question3choice' + str(protein) + '"]')
	en.click()
	options = {
		2: "Lose Weight",
		3: "Meal Supplement",
		4: "Build Muscle",
		5: "Maintain Muscle",
		6: "Look Bigger",
		7: "Recover After Workouts",
		8: "Sports Performance",
		9: "Increase Calorie Intake"
	}
	fileHandler.write(PREFIX_TAB + "Why take Protein Powder : " + options[protein] + NEW_LINE)
	en.send_keys(Keys.ENTER)
	time.sleep(TIME)
	
	# Used Protein Before ?
	used_powder = random.choice([1, 2])
	en = driver.find_element_by_xpath("//*[@id='question5choice" + str(used_powder) + "']")
	en.click()
	fileHandler.write(PREFIX_TAB + "Used Protein Powder Before : " + ("Yes" if used_powder == 1 else "No") + NEW_LINE)
	en.send_keys(Keys.ENTER)
	time.sleep(TIME)
	
	# When will you take Protein Powder
	time_protein = random.choice([0, 1, 2, 3, 4, 5, 6])
	options = {
		0: "During Exercise",
		1: "After Waking Up",
		2: "Before Exercise",
		3: "After Exercise",
		4: "Before Bed",
		5: "I'm not sure",
		6: "Whenever I can"
	}
	en = driver.find_element_by_xpath("//*[@id='question10choice" + str(time_protein) + "']")
	en.click()
	fileHandler.write(PREFIX_TAB + "Time to take Protein Powder : " + options[time_protein] + NEW_LINE)
	en.send_keys(Keys.ENTER)
	time.sleep(TIME)
	
	# Hours of Sleep
	en = driver.find_element_by_xpath('//*[@id="question_form"]/div/input')
	move = ActionChains(driver)
	move.click_and_hold(en).move_by_offset(0, 0).release().perform()
	en.send_keys(Keys.ENTER)
	fileHandler.write(PREFIX_TAB + "Hours of Sleep : " + driver.find_element_by_xpath(
		'//*[@id="question_form"]/div/output').text + NEW_LINE)
	time.sleep(TIME)
	
	# Meals each day
	meals = random.choice([1, 2, 3])
	en = driver.find_element_by_xpath("//*[@id='question81choice" + str(meals) + "']")
	en.click()
	options = {
		1: "2 or  Less",
		2: "3",
		3: "4 or More"
	}
	fileHandler.write(PREFIX_TAB + "Meals Each Day : " + options[meals] + NEW_LINE)
	en.send_keys(Keys.ENTER)
	time.sleep(TIME)
	
	# Dietary Restrictions
	rest = 8
	en = driver.find_element_by_xpath("//*[@id='question11choice" + str(rest) + "']")
	en.click()
	options = {
		1: "Vegan",
		2: "Vegetarian",
		3: "Gluten Allergy",
		4: "Lactose Intolerant",
		5: "Soy Allergy",
		6: "Whey Allergy",
		7: "Other",
		8: "None"
	}
	en.send_keys(Keys.ENTER)
	fileHandler.write(PREFIX_TAB + "Dietary Restrictions : " + options[rest] + NEW_LINE)
	time.sleep(TIME)
	
	# Flavor
	flavor = random.choice([1, 2])
	en = driver.find_element_by_xpath("//*[@id='question12choice" + str(flavor) + "']")
	en.click()
	fileHandler.write(PREFIX_TAB + "Preferred Flavor :" + ("Chocolate" if flavor == 1 else "Vanilla") + NEW_LINE)
	en.send_keys(Keys.ENTER)
	time.sleep(TIME)
	
	# Find about Gainful
	en = driver.find_element_by_xpath("//*[@id='question14choice11']")
	en.click()
	en.send_keys(Keys.ENTER)
	time.sleep(TIME)
	
	# Random Name and Email
	en = driver.find_element_by_id("first_name")
	en.send_keys(random_name())
	en = driver.find_element_by_id("email-form")
	en.send_keys(random_name(), "@", random_name(), '.com')
	en.send_keys(Keys.ENTER)
	time.sleep(TIME + 10)
	
	fileHandler.write(NEW_LINE)
	fileHandler.write("\tOutput" + NEW_LINE)
	for td in driver.find_elements_by_xpath("//*[@id='ingTableBody']/tr/td"):
		fileHandler.write("\t" + td.text if td.text != "" else NEW_LINE)
	fileHandler.write(NEW_LINE)
	driver.quit()

fileHandler.write("-----------------------------------------END-----------------------------------------")