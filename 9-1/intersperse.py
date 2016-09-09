# 9/1 — Intersperse

# Write a function that takes a list of lists and intersperses their elements, e.g
# intersperse([[1,2,3], [4,5,6], [7,8,9]]) => [1,4,7,2,5,8,3,6,9]

def intersperse(mega_list):
	final_list = []
	large_size = 0
	# accounts for lists of different sizes
	for mini_list in mega_list:
		if len(mini_list) > large_size:
			large_size = len(mini_list)

	for i in range(0, large_size):
		for mini_list in mega_list:			
			if len(mini_list) > i:
				final_list.append(mini_list[i])

	print final_list

intersperse([[1,2,3], [4,5,6], [7,8,9]])