
def average (text):
	letter_count = 0
	word_count = 0
	for words in text:
		words = words.replace('.', '')
		words = words.replace(',', '')
		words = words.split()
		word_count = len(words)
		for word in words:
			letter_count += len(word)

	return float('%.2f' % (letter_count / word_count))

def main ():

	with open('38.txt', 'r') as file:
		print ('Average word length:', average(file))

main()