import random
import os
import itertools

alpha = []
for x in range(97, 123):
	alpha.append(chr(x))

name = ""

for x in range(random.randint(5, 9)):
	name += random.choice(alpha)

print("Name : ", name)

print(os.name)

print(list(itertools.permutations([1, 2, 3, 4], 2)))


def random_year():
	year = []
	for x in range(1900, 2000):
		year.append(x)
	
	return random.choice(year)


print(random_year())


def random_gender():
	options = ["Male", "Female"]
	return random.choice(options)


for x in range(10):
	print(random_gender())


options = {1: "weightlifting", 2: "Cardio", 3: "Sports", 4: "Yoga", 5: "Dance", 6: "Swimming", 7: "Others"}
