def find_longest_word (l):
	largest_word = 1
	word = ""
	for i in l:
		if len(i) > largest_word:
			word = i
			largest_word = len(i)
	return word, largest_word
		


def main ():
	words =["Humberto", "Daniel", "Jaime"]

	print (find_longest_word(words))


main()	