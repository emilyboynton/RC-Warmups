# 8-24:
# rank: write a function that takes a file name 
# and a character, and prints the lines in the file,
# ordered by the number of times the character appears in each line.

# foo.txt
# hey,
# hello world!
# how's everyone doing?

# rank('foo.txt', 'e')
# -->	how's everyone doing?
#		hey,
#		hello world!

def rank(filename, char):
	lines = []
	with open(filename, 'r') as f:
		for line in f:
			count = 0
			for word in line.split():
				count += count_char(word, char)
			lines.append((line, count))
	lines = sorted(lines, key=lambda line: line[1], reverse = True)
	for line in lines:
		print line[0]


def count_char(word, char):
	count = 0
	for i in word:
		if i == char:
			count += 1
	return count

rank('foo.txt', 'e')

