
def intersperse(mega_list):
	final_list = []
	large_size = 0
	
	for mini_list in mega_list:
		if len(mini_list) > large_size:
			large_size = len(mini_list)

	for i in range(0, large_size):
		for mini_list in mega_list:			
			if len(mini_list) > i:
				final_list.append(mini_list[i])

	print final_list

intersperse([[1,2,3], [4,5,6], [7,8,9]])