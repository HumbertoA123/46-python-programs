def sum_nums (l):
	nums = 0
	for i in l:
		nums += i
	return nums

def mult_nums (l):
	nums = 1
	for i in l:
		nums *= i 
	return nums


def main ():
	numbers = [1, 2, 3, 4]
	print (sum_nums(numbers))
	print (mult_nums(numbers))

main()