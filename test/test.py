

names = ['철수', '영희', '동희', '영수', '철수', '민영']
sex = ['남', '여', '남', '남', '남', '여']

data = {}
x = []
y = []
label = 0
for i in range(len(names)) : 
	# x 
	if names[i] in data : 
		value = data[names[i]]
		x.append(value)

	else : 
		data.setdefault(names[i], label)
		x.append(label)
		label+=1 
	
	# y 
	if sex[i] =='남' :
		y.append(0)
	elif sex[i] =='여' :
		y.append(1)

print(data)
print(x)
print(y)