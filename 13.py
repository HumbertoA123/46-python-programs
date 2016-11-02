def max_in_list (array):
	bubble = 1
	sort = False
	while  sort == False:
	#This while condition will run until sort = True.
		sort = True
		for i in range(len(array) - 1):
			if array[i] > array[i + 1]:
				array[i], array[i + 1] = array[i + 1], array[i]
				sort = False
				bubble += 1
		return array[-1]


def main ():

	print (max_in_list([1, 2, 3, 4, 10, 4, 200, 3]))

main()