def overlapping (a, b):
	for i in a:
		for j in b:
			if i == j:
				return True
	else:
		return False

def main ():
	print (overlapping([1, 2, 3, 4], [4, 5, 6, 7] ))
	print (overlapping([1, 2, 3, 4], [5, 6, 7] ))



main()