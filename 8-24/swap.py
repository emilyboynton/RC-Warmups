# 8/24
# swap: write a function that takes two lists: 
# L1 contains pairs of numbers. For each pari in L2,
# swap the corresponding elemets in L1, and return the 
# result at the end

# swap(['a', 'b', 'c'], [(0,2),(1,2)])
# --> ['c', 'a', 'b']

def swap(list_one, list_two):
	first = 0
	second = 0
	temp = 0
	for pair in list_two:
		(first, second) = pair
		temp = list_one[first]
		list_one[first] = list_one[second]
		list_one[second] = temp
	print list_one

swap(['a', 'b', 'c'], [(0,2),(1,2)])