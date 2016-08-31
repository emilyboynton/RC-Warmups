# 8-25
# Merge: write a function that takes a list of sorted lists of numbers
# and returns a single sorted list with all of the numbers.
# Don't use your language's sort funtion

# merge([[1, 5, 7], [3, 4, 9]])
# --> [1, 3, 4, 5, 7, 9]

def merge(mega_list):
	final_list = []

	for l in range(0, len(mega_list)):
		if final_list != []:
			for j, num in enumerate(mega_list[l]):
				v = 0
				while num > final_list[v] and final_list[v] != final_list[-1]:
					v += 1
				final_list.insert(v, num)
		else:
			final_list = mega_list[l]

		if final_list[-1] < final_list[-2]:
			temp = final_list[-1]
			final_list[-1] = final_list[-2]
			final_list[-2] = temp

	return final_list

print merge([[1, 5, 7], [3, 4, 9], [32, 7, 0]])