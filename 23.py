def correct (s):
	s = " ".join(s.split())
	l = []
	for i in range(len(s)):
		if s[i] == '.' and s[i + 1] != ' ':
			l.append('. ')
		else:
			l.append(s[i])
	return "".join(l)



def main ():

	text = "Humberto     house.hi"
	print (correct(text))

main()