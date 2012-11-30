#!/usr/bin/python


import sys

zahlen = []
palindorms = []

for x in range(1,1000):
	for y in range(1,1000):
		zahlen.append(x*y)

zahlen.sort()
zahlen.reverse()

for x in zahlen:
	a = []
	zahl = x
	digit = False
	for y in (100000,10000,1000,100,10,1):
		if x/y != 0 or digit == True:
			digit = True	
			a.append(x/y)	
			x=x-(x/y)*y
	error=0
	for z in range(0,(len(a)-(len(a)%2))/2):
		if a[z]!=a[len(a)-1-z]:
			error += 1
	if error == 0:
		print zahl
		sys.exit(2)
