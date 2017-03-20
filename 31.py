def Map (func, ls):
	result = []
	for i in ls:
		result.append(func(i))
	return result

def Reduce (func, ls):
	result = ls[0]
	for i in ls[1:]:
		result = func(result, i)
	return result

def Filter (func, ls):
	result = []
	for i in ls:
		if func(i):
			result.append(func(i))
	return result


def main ():

	lst = [1, 2, 3, 4, 5, 3, 1000, 4]
	print (Map(lambda a : a**2, lst))

	print (Reduce(lambda a, b : a if a > b else b, lst))

	print (Filter(lambda a : a if a % 2 == 0 else None, lst))

main()