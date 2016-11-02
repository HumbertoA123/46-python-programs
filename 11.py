def generate_n_chars(n, char):
	new_string = ""
	for i in range(n + 1):
		new_string = new_string + char
	return new_string


def main ():
	print (generate_n_chars(10, "X"))


main()