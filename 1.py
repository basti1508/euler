multiples = []
for x in range(1,1000):
	if x%3 == 0 or x%5 == 0:
		multiples.append(x)
res = 0
for x in multiples:
	res += x
print res
