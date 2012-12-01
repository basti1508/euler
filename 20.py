#!/usr/bin/python

number = 100
product = 100 

while number > 0:
	product = product * number
	number -= 1

product = str(product)
result = 0
for x in product:
	result = result + int(x)
print result
