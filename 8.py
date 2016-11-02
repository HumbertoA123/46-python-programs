def is_palindrome (s):
	s = s.lower()
	rev_s = s[::-1]
	if s == rev_s:
		return True
	else:
		return False

def main ():
	print (is_palindrome("Radar"))


main()