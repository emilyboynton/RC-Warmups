# 8/25
# Splitby: write a function that takes a filename and a list of words,
# and returns a list of strings that appear in the file between occurances 
# of the words in the list.

# foo.txt:
# This is an example- I am excited!

# splitby('foo.txt', ['am', 'is'])
# --> ['this',
#		'an example- I',
#		'excited!']

def splitby(filename, list_strings):
	indexes = []
	final_list = []
	little_list = []
	with open(filename, 'r') as f:
		for line in f:
			word_list = [word for word in line.split()]
		
		indexes = [(word_list.index(string)) for string in list_strings]

		for i, word in enumerate(word_list):
			if i not in indexes:
				little_list.append(word)
			else:
				final_list.append(' '.join(little_list))
				little_list = []
		final_list.append(' '.join(little_list))

		return final_list



print splitby('foo.txt', ['am', 'is'])

