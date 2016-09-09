# 8-31: FASS2 (Fizzbuzz As A Service startup)

# Choose a custom string to be printed instead of numbers
# faas2("blorp") prints:
# blorp
# blorp
# fizz
# blorp
# buzz
# fizz
# blorp
# blorp
# fizz
# buzz
# blorp
# fizz
# blorp
# blorp
# fizzbuzz
# ...

def faas2(my_string):
	for i in range(1,101):
		printable = ""
		if i % 3 == 0:
			printable += "fizz"
		if i % 5 == 0:
			printable += "buzz"
		if i % 3 != 0 and i % 5 != 0:
			printable += my_string
		print printable
faas2("blorp")