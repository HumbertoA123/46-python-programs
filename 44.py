from random import randrange
import re
def brackets(n):
	i, result, brackets = 0, '', '[]'
# Add brackets in an arbitrary order
	while i < n*2:
		result += brackets[randrange(len(brackets))]
		i+=1
# Save our string of brackets
	bracket_string = result
# Remove all found pairs of brackets using regex
	while len(re.findall(r'\[\]', result)) > 0:
		result = re.sub(r'\[\]', '', result)
# If after removing all pairs of brackets the string is still not empty
	if len(result) > 0:
		print (bracket_string, 'NOT OK')
	else:
		print (bracket_string, 'OK')
#test
brackets(3)