# Bunnies, 8/3

# Write a function that takes a starting number of bunnies and a litter size, 
# and prints out the number of bunnies in the first 20 generations. Remember that bunnies
# reproduce asexually and are immortal.

# bunnies(5, 3)
# 5		# baby bunnies
# 5		# adolescent bunnies
# 20 	# 5 adults + 15 babies
# 35 	# 5 adults + 15 adolescents + 15 babies
# 95 	# etc...

def bunnies(start_num, litter_size):
	adults = 0
	adolescents = 0
	babies = start_num
	total_bunnies = adults + adolescents + babies
	print total_bunnies

	for i in range(19):
		adults += adolescents
		adolescents = babies
		babies = adults * litter_size
		total_bunnies = adults + adolescents + babies
		print total_bunnies

bunnies(5, 3)



