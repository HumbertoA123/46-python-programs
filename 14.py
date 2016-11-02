def words_len (l):
	lengths = {}
	for i in l:
		lengths.update({i : len(i)})
	return lengths


def main ():
	words =["Humberto", "Daniel", "Jaime"]

	print (words_len(words))


main()	