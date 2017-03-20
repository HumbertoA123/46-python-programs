
def hapax (file):
	hapaxes = []
	word_freq = {}
	for n in file:
		n = n.strip()
		n = n.lower()
		n = n.replace('.', '')
		n = n.replace(';', '')
		n = n.replace(',', '')
		n = n.replace('"', '')
		n = n.split()

		for word in n:
			if word in word_freq:
				word_freq[word] += 1
			else:
				word_freq[word] = 1
		for element in word_freq:
			if word_freq[element] == 1:
				hapaxes.append(element)
	return hapaxes



def main ():

	with open('36.txt', 'r') as text:
		print ('Hapaxes: ', hapax(text))

main()