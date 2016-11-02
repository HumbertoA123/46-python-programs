def is_member (x, a):
	if x in a:
		return True
	else:
		return False


def main ():
	print (is_member(1, [1, 2, 3, 4]))
	print (is_member(5, [1, 2, 3, 4]))
main()