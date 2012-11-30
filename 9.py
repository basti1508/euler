#!/usr/bin/python

import sys

a = 0
b = 0
c = 0
while True:
	for x in range(0,1001):
		a = x
		for y in range(0,1001):
			b = y
			for z in range(0,1001):
				c = z
				if a+b+c > 1000:
					break
				else:
					if (a*a)+(b*b)==(c*c) and a+b+c == 1000:
						print a*b*c
