# 8/29 - press

# Write a function that takes a string, and encrypts it as follows:

# find the most common three character sequence that appears in the string.
# find a character that does not appear in the string
# replace the sequence with the character everywhere it appears in the string, 
# then put them both at the beginning of the string so it's 
# possible to get the original back
# Example:

# press("Excellent bells ring pellucidly") -> "ellZExcZent bZs ring pZucidly"

def press(my_string):
	substr = ''
	count = 0
	for i in range(0, len(my_string))