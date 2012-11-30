#!/usr/bin/python

import sys

number = 0
prime = 0

while True:
	number += 1
	error=0
	for x in range(1,number+1):
		if x!=1 and x!=number and number%x==0:
			error += 1
			break
	if error == 0:
		prime +=1
		#print str(prime)+" -- "+str(number)
	if prime == 10002:
		print number
		sys.exit(2)
	if prime % 100 == 0:
		print prime
