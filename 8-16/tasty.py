# 8/16
# tasty: write a function that takes a recipe and a number n,
# and outputs n times the recipe with appropriate unit conversions.

# units:
# 3t = 1T
# 16T = 1c
# 4c = 1q

# example:
# tasty(2,  {'mayonnaise': (2, 'c')
#			'brown sugar': (8, 'T')
#			'cayenne': (2, 't')})
# -->
# 
# {'mayonnaise': (1, 'q')
# 'brown sugar'}: (1, 'c')
# 'cayenne': (1.33, 'T')

from __future__ import division

recipe = {'mayonnaise': (2, 'c'),
'brown sugar': (8, 'T'),
'cayenne': (2, 't')}

conv_table = {'t' : (3, 'T'),
'T': (16, 'c'),
'c' : (4, 'q')}

def tasty(num, recipe_dict):
	new_dict = {}
	for ingredient, instructions in recipe_dict.iteritems():
		amount, unit = instructions
		amount *= num
		
		new_dict[ingredient] = conv_meas(amount, unit)

	return new_dict

def conv_meas(amount, unit):
	if unit not in conv_table:
		return (amount, unit)

	max_meas, new_unit = conv_table[unit]

	if amount >= max_meas:
		amount /= max_meas
		conv_meas(amount, new_unit)

	return (amount, new_unit)

print tasty(2, recipe)
