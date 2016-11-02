def char_freq (chars):
	frecuency = {}
	for i in range(len(chars)):
		if chars[i] not in frecuency:
			frecuency[chars[i]] = 1
		elif chars[i] in frecuency:
			frecuency[chars[i]] = frecuency[chars[i]] + 1
	return frecuency



def main ():

	s = "abcabcabcccccccc"
	print (char_freq(s))

main()