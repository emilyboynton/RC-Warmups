# 8/17 
# lossy: write a function that takes an ascii string, 
# and replaces all adjacent characters of the same type with the
# first character of that type. The 3 types are consonants, vowels, 
# and other (whitespace, punctuation, etc)

# lossy("Spring beets - $2/each!")
# --> "Sin bet ec!"

import string

blah = list(string.ascii_letters)
vowels = list("aeiouAEIOU")

my_string = "Spring beets - $2/each!"

def determine_type(char):
	if char in vowels:
		return "vowel"
	if char in blah:
		return "cons"
	else:
		return "other"

def lossy(my_string):
	curr_let = 0
	next_let = 1
	new_string = []

	while next_let < len(my_string):
		if determine_type(my_string[curr_let]) == determine_type(my_string[next_let]):
			my_string = my_string[0:curr_let + 1] + my_string[next_let+1: ]
			print my_string
		else:
			curr_let += 1
			next_let += 1

	print my_string

lossy(my_string)



