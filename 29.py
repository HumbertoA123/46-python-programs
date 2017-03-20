words = ['Humberto', 'Dolphin', 'Whale', 'Kindergarden']

def filter_long_words (n, words):
	print (list(filter(lambda word : word if len(word) <= n else None, words)))


def main ():

	filter_long_words(8, words)

main()