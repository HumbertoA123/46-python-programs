def is_vowel (char):
	vowels = ["a", "e", "i", "o", "u"]
	if char.lower() in vowels:
		return True
	else:
		return False


def main ():
	print (is_vowel("A"))
	print (is_vowel("G"))

main()