import random
import os

alpha = []
for x in range(97, 123):
	alpha.append(chr(x))

name = ""

for x in range(0, 5):
	name += random.choice(alpha)

print("Name : ", name)


print(os.name)