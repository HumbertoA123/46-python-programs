import random

def anagram (word, words):
	count = 0
	for i in range(50):
		random.shuffle(word)
		new_word = ''.join(word)
		if new_word in words and len(new_word):
			count += 1
	return count




def main ():

	with open ('43.txt') as file:
		words = []
		for line in file:
			line = line.replace('\n', '')
			words.append(line)
		new_words = []
		for word in words:
			new_word = []
			for char in word:
				new_word.append(char)
			new_words.append(new_word)

			result = anagram(new_word, words)


			if result >= 1:
				print (word, result)

main()