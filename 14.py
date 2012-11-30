#!/usr/bin/python

import sys

start = 2
global_counter = [0,0]
for x in range(1,999998):
	seq_start= start+x
	counter = 0
	if x % 1000 == 0:
		print x
	while seq_start != 1:
		if seq_start%2 == 0:
			seq_start = seq_start/2
		else:
			seq_start = 3*seq_start + 1
		counter += 1
	if counter > global_counter[1]:
		global_counter[1] = counter
		global_counter[0] = x
	
print "number: \t"+str(global_counter[0]+2)+" --> "+str(global_counter)


