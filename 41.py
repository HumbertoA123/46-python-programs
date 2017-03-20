import random

def lingo (word):
	while True:
		guess = []
		var = input()
		word = list(word)
		for char in range(len(var)):
			if var[char] in word:
				guess.append('(' + var[char] + ')')
			else:
				guess.append(var[char])
		guess = ''.join(guess)
		word = ''.join(word)
		print ('Clue:', guess)
		if word == var:
			print ('Correct!')
			break


def main ():

	words = ['lingo', 'water', 'tiger', 'brown', 'black', 'paper', 'juice']
	word = words.pop(random.randrange(0, len(words)))
	
	lingo(word)



main()