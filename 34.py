def char_freq_table (text):
	freq = {}
	for s in text:
		s = s.lower()
		for char in s:
			if char in freq:
				freq[char] += 1
			else:
				freq[char] = 1
	for i in freq:
		print (i, '=', freq[i])





def main ():

	file = input('Input a text file: ')
	text = open(file)
	char_freq_table(text)


main()