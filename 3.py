def length (s):
	count = 0
	for i in s:
		count += 1
	return count


def main ():
	print (length([1,2,3,4,5,6]))
	print (length("Hello World!"))

main()