# 8/22
# Happy Number: write a function that returns a boolean indicating if a 
# number is a happy number. To do this: 
# 1. replace it with the sum of the squares of its digits
# 2. repeat

# If this process ends with 1, the number is happy. 
# If this process gets stuck in a loop, it is not.

# e.g.
# happy(19) -> True
# happy(11) -> False

loop = 1000

def happy(num):
	num = str(num)
	added = 0
	for digit in num:
		added += int(digit) * int(digit)
	if added == 1:
		return True
	else:
		global loop
		loop -= 1
		if loop > 0:
			return happy(added)
	return False

print happy(19)
print happy(11)