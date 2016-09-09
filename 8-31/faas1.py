# 8/31 - FAAS1

# You are on the research team of a new Fizzbuzz As A Service startup - 
# your job is to write variations on fizzbuzz with tunable parameters 
# for the discerning fizzbuzz connoisseur. Set a timer for 20 minutes 
# (or as long as you want to spend on warmups) and write as many as you can.

# Examples:

# faas1 - customize the incrementation speed
# faas1(1) behaves like fizzbuzz
# faas1(2) prints:
# 1
# fizz
# buzz
# 7
# fizz
# 11
# 13
# fizzbuzz
# .... (whether it goes 100 times or up to 100 is up to you :) )

def faas1(num):
	for i in range(1,101, num):
		printable = ""
	# if i % 3 == 0 and i % 5 == 0:
		if i % 3 == 0:
			printable += "fizz"
		if i % 5 == 0:
			printable += "buzz"
		if i % 3 != 0 and i % 5 != 0:
			printable += str(i)
		print printable
faas1(2)

