terms = [1,2]
while int(terms[len(terms)-1]) < 4000000:
	terms.append(terms[len(terms)-2]+terms[len(terms)-1])
res = 0 
for x in terms:
	if x<4000000 and x%2==0:
		res += x
print res



