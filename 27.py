words = ['Dog', 'Computer', 'Hermosillo', 'Clown']

def first_method (words):
	print ('Using a for loop:')
	words_count = {}
	for word in words:
		for letters_count in range(len(word)):
			if word in words_count:
				words_count[word] += 1
			else:
				words_count = {word : 0}
		print (letters_count + 1, word)


def second_method (words):
	print ('Using map() function:')
	lst = list(map(lambda words : len(words), words))
	print (lst)

def third_method (words):
	print ('Using list comprehension:')
	lst = [len(word) for word in words]
	print (lst)



def main ():

	first_method(words)
	print ('\n')
	second_method(words)
	print ('\n')
	third_method(words)

main()