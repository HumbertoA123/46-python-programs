def is_panagram (s):
	abc = "abcdefghijklmnopqrstuvwxyz"
	for i in abc:
		if i not in s:
			return False
	else:
		return True


def main ():

	s = "The quick brown fox jumps over the lazy dog"
	print (is_panagram(s))

main()