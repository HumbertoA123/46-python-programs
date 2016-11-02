def rot_13 (s, key):
	new_s = []
	for i in s:
		if i == " ":
			new_s.append(" ")
		elif i == '!':
			new_s.append('!')
		elif i == '?':
			new_s.append('?')
		else:
			new_s.append(key[i])
	new_s = "".join(new_s)
	return new_s


def main ():

	text = "Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!"
	key = {'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t', 'h':'u', 
       'i':'v', 'j':'w', 'k':'x', 'l':'y', 'm':'z', 'n':'a', 'o':'b', 'p':'c', 
       'q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h', 'v':'i', 'w':'j', 'x':'k',
       'y':'l', 'z':'m', 'A':'N', 'B':'O', 'C':'P', 'D':'Q', 'E':'R', 'F':'S', 
       'G':'T', 'H':'U', 'I':'V', 'J':'W', 'K':'X', 'L':'Y', 'M':'Z', 'N':'A', 
       'O':'B', 'P':'C', 'Q':'D', 'R':'E', 'S':'F', 'T':'G', 'U':'H', 'V':'I', 
       'W':'J', 'X':'K', 'Y':'L', 'Z':'M'}

	print (rot_13(text, key))


main()