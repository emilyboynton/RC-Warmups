# 8/23
# First Unique Char
# Given a string find the first non-repeating character in if and 
# return its index. Return -1 if there is no non-repeating char

# Examples:
# firstunique("aabcc") --> 2
# first unique("aabbcc") --> -1


def firstunique(my_string):

	for index, char in enumerate(my_string):
		if char in my_string[index+1:] or char in my_string[0:index]:
			continue
		else:
			return index
	return -1

print firstunique("aabcc")
print firstunique("aabbcc")
			