# 9/8: Matches

# Write a function that takes two strings, and returns the number of times 
# the first string appears in the second, without using any of your language's 
# string processing facilities (i.e., treat the strings as lists of characters).

# matches(['baba', 'abababa'])
# -> 2


def matches(list_str):
	tester = list_str[0]
	my_string = list_str[1]
	count = 0
	for index, char in enumerate(my_string):
		i = 0
		while i < len(tester):
			#checks range and then compares
			if index + i < len(my_string) and tester[i] == my_string[index + i]:
				#checks if it is the last in the tester string
				if i == len(tester) - 1:
					count += 1
					break
				i += 1
			else:
				break
			if my_string[index] == my_string[-1]:
				break
	return count

print matches(['baba', 'abababa'])