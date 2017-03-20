import random

def anagram (word):
	new_word = []
	for char in word:
		new_word.append(char)
	
	random.shuffle(new_word)
	return ''.join(new_word)
	
	
	

def main ():

	words = ['brown', 'carpet', 'dirt', 'baseball', 'bottle', 'cup', 'water']

	word = words.pop(random.randrange(0, len(words)))

	print ('Word anagram:', anagram(word))

	while True:
		var = input('Guess the word: ')
		if var == word:
			print ('Correct!')
			break
		else:
			print ('Wrong. Guees again.')

main()