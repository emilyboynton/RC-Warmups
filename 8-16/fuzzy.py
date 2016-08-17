# 8/16 
# fuzzy: write a function that takes two strings, and checks whether the letters of the first
# one appear in order (but not necessarily adjacent) in the second.

# fuzzy('abc', 'a baby cat') --> True
# fuzzy('abc', 'acbb') --> False

def fuzzy(str_one, str_two):

	next_num = 1
	curr_num = 0

	while next_num < len(str_one):
		if str_two.find(str_one[next_num][0:]) > str_two.find(str_one[curr_num][0:]):
			next_num += 1
			curr_num += 1
		else:
			return False

	return True


print fuzzy('abc', 'abbbc')
