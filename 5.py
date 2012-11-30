#!/usr/bin/python

import sys

a=0
list = range(1,21)
list.reverse()

while True:
	a += 20
	error = 0
	for x in list:
		if a%x != 0:
			error += 1
			break
	if error==0:
		print a
		sys.exit(2)
			
