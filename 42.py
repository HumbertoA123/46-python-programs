
def sentence_splitter (text):
	new_text = []
	for sentence in text:
		for char in range(len(sentence) - 2):
			#if sentence[char] == '.' and sentence[char - 2].istitle():
			#	new_text.append(sentence[char - 2 : char + 1])

			if sentence[char] == '.' and sentence[char + 1] == ' ' \
			and sentence[char + 2].istitle():
				if sentence[char - 2].istitle():
					new_text.append(sentence[char] + sentence[char + 1])
				else:
					new_text.append(sentence[char] + sentence[char + 1] + '\n')

			elif sentence[char] == '?' and sentence[char + 1] == ' ' \
			and sentence[char + 2].istitle():
				new_text.append(sentence[char] + sentence[char + 1] + '\n')

			else:
				new_text.append(sentence[char])

		new_text.append(sentence[char + 1] + sentence[char + 2])
		text = ''.join(new_text)
	print (text)



def main ():

	with open('42.txt') as file:
		sentence_splitter(file)

main()