import time
import os
import random
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

fileName = "output/" + str(time.strftime("%H-%M-%S___%d-%m-%Y")) + ".txt"
TIME = 7
PREFIX_TAB = "\t\t"
NEW_LINE = "\n"


def random_gender():
	return random.choice(["Male", "Female"])


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
	for x in range(1, 28):
		date.append(x)
	
	return random.choice(date)


def random_month():
	month = []
	for x in range(1, 13):
		month.append(x)
	
	return random.choice(month)


def question_exercise():
	return random.choice([1, 2, 3])


def question_sports():
	return random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])


def question_type_exercise():
	return random.choice([1, 2, 3, 4, 5, 6, 7])


def slider_random():
	return random.choice([-250, -160, -120, -60, 0, 60, 120, 160, 250])


def protein_powder_take():
	return random.choice([1, 2, 3, 4, 5, 6, 7, 8])


# Open File
fileHandler = open(fileName, "a")

for x in range(1, 31):
	if os.name == "posix":
		driver = webdriver.Chrome(executable_path="/Users/akasharora/PycharmProjects/Web-Scrapping/chromedriver")
	else:
		driver = webdriver.Chrome('chromedriver.exe')
	fileHandler.write("***********************************************************************************" + NEW_LINE)
	fileHandler.write("Test #" + str(x) + NEW_LINE)
	fileHandler.write("\tInputs" + NEW_LINE)
	# Open Link
	gender = random_gender()
	fileHandler.write(PREFIX_TAB + "Gender : " + gender + NEW_LINE)
	driver.get("https://www.gainful.com/consultation/?gender=" + gender)
	time.sleep(TIME)
	# Select Input -> Gender
	elem = driver.find_element_by_id("question7choice1")
	elem.submit()
	driver.get("https://www.gainful.com/consultation/?gender=" + gender)
	time.sleep(TIME)
	
	# Select DOB
	month = str(random_month())
	day = str(random_date())
	year = str(random_year())
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
	move.click_and_hold(en).move_by_offset(slider_random(), 0).release().perform()
	fileHandler.write(PREFIX_TAB + "Current Body Type : " + driver.find_element_by_xpath(
		"//*[@id='question_form']/div[1]/output").text + NEW_LINE)
	time.sleep(TIME)
	en = driver.find_element_by_xpath("//*[@id='question_form']/div[1]/section/input")
	move = ActionChains(driver)
	move.click_and_hold(en).move_by_offset(slider_random(), 0).release().perform()
	fileHandler.write(PREFIX_TAB + "Goal Body Type :" + driver.find_element_by_xpath(
		"//*[@id='question_form']/div[1]/section/output").text + NEW_LINE)
	en.send_keys(Keys.ENTER)
	time.sleep(TIME)
	
	# Physical Attributes -> Height / Current Weight / Goal Weight
	en = driver.find_element_by_xpath("//*[@id='question_form']/div/input")
	move = ActionChains(driver)
	move.click_and_hold(en).move_by_offset(slider_random(), 0).release().perform()
	fileHandler.write(
		PREFIX_TAB + "Height : " + driver.find_element_by_xpath("//*[@id='question_form']/div/output").text + NEW_LINE)
	en = driver.find_element_by_xpath("//*[@id='question_form']/div/section/input")
	move = ActionChains(driver)
	move.click_and_hold(en).move_by_offset(slider_random(), 0).release().perform()
	fileHandler.write(PREFIX_TAB + "Current Weight : " + driver.find_element_by_xpath(
		"//*[@id='question_form']/div/section/output").text + NEW_LINE)
	en = driver.find_element_by_xpath("//*[@id='question_form']/section/input")
	move = ActionChains(driver)
	move.click_and_hold(en).move_by_offset(slider_random(), 0).release().perform()
	fileHandler.write(PREFIX_TAB + "Goal Weight : " + driver.find_element_by_xpath(
		"//*[@id='question_form']/section/output").text + NEW_LINE)
	en.send_keys(Keys.ENTER)
	time.sleep(TIME)
	
	# Exercise -> Times a week
	exercise = question_exercise()
	en = driver.find_element_by_xpath('//*[@id="question8choice' + str(exercise) + '"]')
	en.click()
	ex_text = "1 or Less" if exercise == 1 else "2-3" if exercise == 2 else "4 or more"
	fileHandler.write(PREFIX_TAB + "Exercise @ Times/Week : " + ex_text + NEW_LINE)
	en.send_keys(Keys.ENTER)
	time.sleep(TIME)
	
	# Type of Exercise
	type_ex = question_type_exercise()
	en = driver.find_element_by_xpath("//*[@id='question9choice" + str(type_ex) + "']")
	options = {1: "weightlifting", 2: "Cardio", 3: "Sports", 4: "Yoga", 5: "Dance", 6: "Swimming", 7: "Others"}
	fileHandler.write(PREFIX_TAB + "Type of Exercise : " + options[type_ex] + NEW_LINE)
	en.click()
	en.send_keys(Keys.ENTER)
	time.sleep(TIME)
	
	# Sub Sports -> Games
	if type_ex == 3:
		sport = question_sports()
		en = driver.find_element_by_xpath('//*[@id="question1choice' + str(sport) + '"]')
		options = {
			1: "Soccer",
			2: "Football",
			3: "Baseball",
			4: "Basketball",
			5: "Tennis",
			6: "Cricket",
			7: "Rugby",
			8: "Volleyball",
			9: "Hockey",
			10: "Track & Field",
			11: "Gymnastics",
			12: "Swimming",
			13: "Water Polo",
			14: "Other"
		}
		fileHandler.write(PREFIX_TAB + "Sports You Play : " + options[sport] + NEW_LINE)
		en.click()
		en.send_keys(Keys.ENTER)
		time.sleep(TIME)
	
	# Why take Protein Powder
	protein = protein_powder_take()
	en = driver.find_element_by_xpath('//*[@id="question3choice' + str(protein) + '"]')
	en.click()
	options = {
		1: "Lose Weight",
		2: "Meal Supplement",
		3: "Build Muscle",
		4: "Maintain Muscle",
		5: "Look Bigger",
		6: "Recover After Workouts",
		7: "Sports Performance",
		8: "Increase Calorie Intake"
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
	move.click_and_hold(en).move_by_offset(slider_random(), 0).release().perform()
	en.send_keys(Keys.ENTER)
	fileHandler.write(PREFIX_TAB + "Hours of Sleep : " + driver.find_element_by_xpath(
		'//*[@id="question_form"]/div/output').text + NEW_LINE)
	time.sleep(TIME)
	
	# Meals each day
	meals = question_exercise()
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
	rest = protein_powder_take()
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
	time.sleep(TIME+10)
	
	fileHandler.write(NEW_LINE)
	fileHandler.write("\tOutput" + NEW_LINE)
	for td in driver.find_elements_by_xpath("//*[@id='ingTableBody']/tr/td"):
		fileHandler.write("\t" + td.text if td.text != "" else NEW_LINE)
	fileHandler.write(NEW_LINE)
	driver.quit()
	
	
fileHandler.write("-----------------------------------------END-----------------------------------------")
