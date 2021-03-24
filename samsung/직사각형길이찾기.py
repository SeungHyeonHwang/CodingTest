rectangle = list(map(int, input().split()))
dictionary = {}
for rect in rectangle:
	if rect not in dictionary.keys():
		dictionary.setdefault(rect, 1)
	else : 
		del dictionary[rect]

print(list(dictionary.keys())[0])
