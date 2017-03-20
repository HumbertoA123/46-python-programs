

def translate (s):
	translates = {"merry":"god", "christmas":"jul", "and":"och",
				  "happy":"gott", "new":"nytt", "year":"år"}
	if s in translates:
		return translates[s]


def main ():

	card = "merry christmas and happy new year"
	card = card.split()

	print (list(map(translate, card)))

main()