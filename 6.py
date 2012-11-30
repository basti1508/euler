#!/usr/bin/python

sq = 0
su = 0
for x in range(1,101):
	sq += (x*x)
	su += x
su = su*su
print su-sq

