import functools
'''
If you are using python 3 you will have to import the functools module to use
the reduce() function. If you are using python2 you don't have to do anything.
'''

def find_longest_word (lst):
	longest_word = functools.reduce(lambda a, b : (a, len(a))if len(a) > len(b) else b, lst)
	print (longest_word)


def main ():

	lst = ['Donkey', 'Balloon', 'Elephant', 'Book']
	find_longest_word(lst)

main()