def make_ing_form (s):
	exceptions = ['be', 'see', 'flee', 'knee']
	vowel = ['a', 'e', 'i', 'o', 'u']
	if s[-2:] == 'ie':
		s = s.replace(s[-2:], 'y') + 'ing'
	elif s[-1] == 'e' and s not in exceptions:
		s = s[:-1] + 'ing'
	elif s[-3] not in vowel and s[-2] in vowel and s[-1] not in vowel:
		s  = s + s[-1] + 'ing'
	else:
		s = s + 'ing'
	return s




def main ():

	verb = input('Write an infinitive verb to convert it to present participle: ')
	print (make_ing_form(verb))

main()