# 9/6: straight

# WRite a function that takes a list of numbers and returns the longest
# consecutive sublist of strictly increasing or decreasing numbers.

# straight([1, 3, 3, 5, 6, 4, 2, 1, 7])
# --> [6, 4, 2, 1]

def straight(list_num):
	count = 0
	index = 0
	new_count = 0
	run_index = 0
	temp = 0

	while index < len(list_num)-1:
		if list_num[index] < list_num[index + 1]:
			temp = index
			index, new_count = increasing(index, list_num)
			run_index, count = check(new_count, count, temp, run_index)
		elif list_num[index] > list_num[index + 1]:
			temp = index
			index, new_count = decreasing(index, list_num)
			run_index, count = check(new_count, count, temp, run_index)
		else:
			index += 1

	print list_num[run_index: run_index + count]


def check(new_count, count, temp, run_index):
	if new_count > count:
		print new_count, "is bigger than", count
		count = new_count
		run_index = temp
	return run_index, count

def increasing(index, list_num):
	count = 1

	while list_num[index] < list_num[index + 1]:
		index += 1
		count += 1
		if list_num[index] == list_num[-1]:
			break

	return index, count


def decreasing(index, list_num):
	count = 1
	while list_num[index] > list_num[index + 1]:
		index += 1
		count += 1
		if list_num[index] == list_num[-1]:
			break
	return index, count


straight([1, 3, 3, 5, 6, 4, 2, 1, 7])