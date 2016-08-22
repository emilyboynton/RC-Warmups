# 8/22
# Piggy: Write a function that takes a string and encodes it in pig latin
# Move all consonants at the beginning of each word to the end,
# and if it then ends in a consonant, append -'ay'

# piggy('This is a string, yeah?')
# -->'Isthay isay a ingstray, eahyeay?'

# y is always a consonant, and you should capitalize any words that were
# capitalized in the original

import string

vowels = list("aeiouAEIOU")
punctuation = list(string.punctuation)
latin = 'ay'

def latinize(word):
	return word + latin

def get_new_word(word):
	move_cons = ''
	if word[0] not in vowels: 	#starts with consonant
	# collect the consonants in order to append at end
		for char in word:
			if char not in vowels:
				move_cons += char
			else:		# have hit a vowel
				return word[len(move_cons):] + move_cons
	if word[-1] in vowels:	# starts with vowel, and ends with a vowel
		return False
	return word 	# this return satisfies the case starts with vowel, ends with cons

def piggy(my_string):
	words = my_string.split()
	for word in words:
		hold_punct = ''
		if word[-1] in punctuation:
			# remove from word, and hold punctuation 
			hold_punct = word[-1]
			word = word[0:-1]
		
		new_word = get_new_word(word)
		if new_word:
			if any(ch.isupper() for ch in new_word):	#re-capitalize words
				new_word = new_word.title()
			print latinize(new_word) + hold_punct,
		else: 
			print word + hold_punct,

piggy('This is a string, yeah?')