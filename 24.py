def make_3sg_form(s):
	l = ['o', 'ch', 's', 'sh', 'x', 'z']
	if s[-1] == 'y':
		s = s[:-1] + 'ies'
	elif s[-1] in l or s[-2:] in l:
		s = s + 'es'
	else:
		s = s + 's'
	return s



def main ():

	verb = input("Write an infinitive verb to convert it to third person: ")
	print (make_3sg_form(verb))

main()