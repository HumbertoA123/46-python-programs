#This program picks a random integer between 1 and 100
#and makes you guess the number.

import random

def random_number ():
	#This function picks a random number between 1 and 100.
	rand = random.randint(1, 20)
	return rand


def main ():
	#Main program.
	rand_num = random_number()

	x = int(input("Guess a number between 1 and 20.\n"))

	count = 1
	guess = False
	while guess is False:
		if x > rand_num:
			x =  int(input("To high! Guess again.\n"))
		if x < rand_num:
			x =  int(input("To low! Guess again.\n"))
		count = count + 1
		guess = False

		if x == rand_num:
			print ("Congratulations! You guess the number in {} guesses.".format(count))
			guess = True



main()