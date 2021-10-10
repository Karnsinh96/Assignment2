def sort_tup(tup):
	tup.sort(key= lambda x:x[-1])
	return tup

tup=[(2,5), (1,2),(4,4), (2,3),(2,1) ]

print(sort_tup(tup))