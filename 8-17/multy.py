# 8/17
# multy: write a function that takes 2 numbers, 
# and returns the smallest prefix of the second that is
# a multiple of the first

# multy(8, 216500) --> 216
# multy(5, 1234) --> None/null/False

def multy(num_one, num_two):
	str_num_two = str(num_two)
	for itr in range(1, len(str_num_two) + 1):
		int_again = int(str_num_two[0:itr])
		if int_again % num_one == 0:
			return int_again
	return False

print multy(8, 216500)
print multy (5, 1234)