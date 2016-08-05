# Given a list of numbers, print out all numbers n that appear between n and 2n (inclusive)
# in the list

# counts([3, 0, 1, 4, 3, 3, 4])

# 1
# 3
# (0 appears too often, 4 not often enough)

count_list = [3, 0, 1, 4, 3, 3, 4]


def counts(count_list):

	count_set = set(count_list)

	for each in count_set:
		num_count = 0
		for num in count_list:
			if each == num:
				num_count += 1
		if num_count >= each and num_count <= 2*each:
			print each

counts(count_list)