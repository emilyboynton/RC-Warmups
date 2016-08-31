
# 8/30 - lifeskills

# You go into a very small grocery store with a fixed amount of money, 
# wanting to spend as much of your budget as possible on a single item. 
# What will you be eating this week, and how much of it can you afford?

# lifeskills(20.04, {'ketchup': 2.99, 'avocados': 0.99, 'milk': 3.25})

# -> ('avocados', 20) # leaving 24 cents

def lifeskills(money, list_dict):
	least_change = money
	least_item = ''
	for i, k in list_dict.iteritems():
		if money % k < least_change:
			least_change = money % k
			least_item = i
	return least_item, round(least_change, 2)


print lifeskills(20.04, {'ketchup': 2.99, 'avocados': 0.99, 'milk': 3.25})