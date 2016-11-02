def bottles_of_beer ():
	for i in range(99, 0, -1):
		print ("""
			{} bottles of beer on the wall, {} bottles of beer.
			Take one down, pass it around, {} bottles of beer on the wall.
			""".format(i, i, i -1))

def main ():

	bottles_of_beer()

main()