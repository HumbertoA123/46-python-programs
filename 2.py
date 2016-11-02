def max_num (x, y, z):
	if x > y and x > z:
		return x
	if y > x and y > z:
		return y
	if z > x and z > y:
		return z

def main ():
	print (max_num(12, 244, 1))

main()