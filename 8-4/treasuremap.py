# Treasure Map 8/4
# Given a hash/dict/map/pairlist that contains rooms with a list of their neighbors,
# write a function that takes a start room and an end room, and returns a path between them,

rooms = {'kit': ['lib', 'bath'],
	'lib': ['bath', 'foyer'],
	'foyer': ['lib', 'din'],
	'din': ['foyer'],
	'bath': ['kit', 'lib']}

def search_map(path_list, end_room):
	this_room = path_list[-1]
	if this_room == end_room:
		return path_list
	for each_room in rooms[this_room]:
		if each_room in path_list:
			continue
		try_path = search_map(path_list + [each_room], end_room)
		if try_path:
			return try_path
			treasuremap(each_room, end_room)

def treasuremap(start_room, end_room):
	# turn start room into path_list[0]
	return search_map([start_room], end_room)


print "final list is", treasuremap('lib', 'kit')
