# 8/22
# mods: write a function that takes a list of numbers, and a number n.
# Split the input list into n lists, where all the elements in each list are the same mod n.

# mods([9, 5, 3, 302], 3)
# --> [
#		[9, 3]  #0 mod 3
#		[] 		# 1 mod 3 -none
#		[5, 302] #2 mod 3
# 	]

def mods(list_nums, n):
	mod_list = []
	for i in range(0,n):
		mod_list.append([])
	for each in list_nums:
		group = each % n
		mod_list[group].append(each)
	return mod_list

print mods([9, 5, 3, 302], 3)