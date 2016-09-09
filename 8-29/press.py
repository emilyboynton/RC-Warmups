# 8/29 - press

# Write a function that takes a string, and encrypts it as follows:

# find the most common three character sequence that appears in the string.
# find a character that does not appear in the string
# replace the sequence with the character everywhere it appears in the string, 
# then put them both at the beginning of the string so it's 
# possible to get the original back
# Example:

# press("Excellent bells ring pellucidly") -> "ellZExcZent bZs ring pZucidly"

import string

def press(my_string):
	max_val = 0
	max_str = ''
	new_char = get_char(my_string)
	list_sub = [my_string[i:i+3] for i in range(0, len(my_string))]
	for index, val in enumerate(list_sub):
		count = 0
		for i in range(index + 1, len(list_sub)):
			if list_sub[i] == val:
				count += 1
			if count > max_val:
				max_val = count
				max_val = val

	for i in range(0, len(my_string)):
		if max_val in my_string:
			my_string = my_string.replace(max_val, new_char)

	print my_string


def get_char(my_string):
	list_lets = list(string.ascii_letters)
	for let in list_lets:
		if let not in my_string:
			return let

press("Excellent bells ring pellucidly")

