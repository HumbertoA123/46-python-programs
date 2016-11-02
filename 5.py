def translate (s):
	vowels = ["a", "e", "i", "o", "u"]
	robber_sentence = ""
	for i in s:
		if i not in vowels:
			robber_sentence += ("{}o{}".format(i, i))
		else:
			robber_sentence += (i)
	print(robber_sentence)



def main ():
	translate("Humberto")

main()