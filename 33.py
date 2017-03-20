def palindrome (word, ls):
	word = word.lower()
	word = word.strip()
	if word[::-1] in ls:
		print (word, word[::-1])



def main ():
	ls = ['desserts', 'diaper', 'semordnilap']
	with open('33.txt') as text:
		for word in text:
			palindrome(word, ls)


main()