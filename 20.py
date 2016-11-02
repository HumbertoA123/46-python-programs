def translate (s):
	new_s = []
	s = s.split()
	translates = {"merry":"god", "christmas":"jul", "and":"och",
				  "happy":"gott", "new":"nytt", "year":"år"}
	for i in s:
		if i in translates:
			new_s.append(translates[i])
	return " ".join(new_s)



def main ():

	card = "merry christmas and happy new year"
	print (translate(card))

main()