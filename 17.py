def is_palindrome (s):
	s = s.lower()
	rev_s = s[::-1]
	if s == rev_s:
		return True
	else:
		return False

def main ():

	phrase = input("Write a word or phrase to check if it is a palindrome.\n")
	phrase = phrase.replace("." or "," or "?" or "¿" or "\'" or "\"" or "!" 
						or ":" or ";", "")
	print (is_palindrome(phrase))


main()