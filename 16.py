#!/usr/bin/python

number = 2

for x in range(1,1000):
	number = number *2

number = str(number)
result = 0
for x in number:
	result = result + int(x)
print result
