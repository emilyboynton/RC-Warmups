# Write a function that takes a filename and a number n, and prints out the
# file contents reversed in chunks of n characters.

# foo.txt contains:
#     hello world
#     how's it going?

# reverser("foo.txt", 3) ->
#     ng?goiit 's howld
#     worlo hel

# Above solution assumes foo.txt does not end in a newline

def reverser(filename, n):
	with open(filename, 'r') as f:
		contents = f.read()

	# since this will be printed in reverse
	start = len(contents) - n
	text = ""
	
	for i in range(start, 0, -n):
		text += ''.join(contents[i:i + n])


	text += contents[0:i]
	print text

reverser("foo.txt", 3)

