# Write a function that takes a string and increments all the numbers that
# appear in it.
# E.g.
# plusone("1+15=16") -> "2+16=17"
# plusone("call me at 3.555-2020") -> "call me at 4.555-2019"


import re

def addone(matchobj):
	s = matchobj.group(0)
	try:
		number = int(s)
	except ValueError:
		number = float(s)
	number += 1
	return str(number)

def plusone(my_string):
	a_string = re.sub(r"\.?\-?[0-9]+\.?[0-9]+", addone, my_string)
	print a_string

plusone("sk35b59.04mm00.88-8.9")
plusone("1+15=16")
plusone("call me at 3.555-2020")