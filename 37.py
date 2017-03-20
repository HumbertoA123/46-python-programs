def main ():

	with open('37.txt') as file:
		with open ('37.2.txt', 'a') as new_file:
			for n, line in enumerate(file):
				new_file.write(str(n + 1) + ' ')
				new_file.write(line + '\n')

main()