def filter_long_words (l, n):
	new_l = []
	for i in l:
		if n < len(i):
			new_l.append(i)
	return new_l


def main():

	words = ["Humberto", "House", "Computer", "Toilet Paper"]
	print (filter_long_words(words, 7))

main()