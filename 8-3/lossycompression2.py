# Lossy Compression 2, 8/3
# Our removing all vowels compression scheme made so much money in 
# Hawaii that the studio has bought a sequel. This time, we're going 
# to read a file, and remove the first and last letters of all words
# that are more than 3 letters. A word is any adjacent series of letters.

# lc2("annakarenina.txt")
# "All app amilie are lik, ac nhapp..."

def lossy_two(filename):
	with open(filename, 'r') as f:
		for line in f:
			for word in line.split():
				if len(word) > 3:
					word = word[1:-1]
				print word

lossy_two("annakarenina.txt")