





import copy
def rotation(dice, name, dirs):
	temp = copy.deepcopy(dice)

	# U O
	if face[name]==0: 
		if dirs =='+':
			for i in range(3):
				dice[1][-1][i] = temp[2][2-i][-1]
				dice[3][i][0] = temp[1][-1][i]
				dice[4][0][i] = temp[3][2-i][0]
				dice[2][i][-1] = temp[4][0][i]
				for j in range(3):
					dice[face[name]][i][j] = temp[face[name]][2-i][j]
		else : 
			for i in range(3):
				dice[4][0][i] = temp[2][i][-1]
				dice[3][i][0] = temp[4][0][2-i]
				dice[1][-1][i] = temp[3][i][0]
				dice[2][2-i][-1] = temp[1][-1][i]
				for j in range(3):
					dice[face[name]][i][j] = temp[face[name]][2-j][i]
	# B O
	elif face[name]==1:
		if dirs =='+':
			for i in range(3):
				dice[5][-1][i] = temp[2][0][2-i]
				dice[3][0][i] = temp[5][-1][2-i]
				dice[0][0][i] = temp[3][0][i]
				dice[2][0][i] = temp[0][0][i]	
				for j in range(3):
					dice[face[name]][i][j] = temp[face[name]][2-j][i]	
		else : 
			for i in range(3):
				dice[3][0][i] = temp[0][0][i]
				dice[0][0][i] = temp[2][0][i]
				dice[2][0][i] = temp[5][-1][2-i]
				dice[5][-1][2-i] = temp[3][0][i]	
				for j in range(3):
					dice[face[name]][i][j] = temp[face[name]][2-j][i]
	# L
	elif face[name]==2:
		if dirs =='+':
			for i in range(3):
				dice[1][i][0] = temp[5][i][0]
				dice[4][i][0] = temp[0][i][0]
				dice[5][i][0] = temp[4][i][0]
				dice[0][i][0] = temp[1][i][0]
		else : 
			for i in range(3):
				dice[1][i][0] = temp[0][i][0]
				dice[4][i][0] = temp[5][i][0]
				dice[5][i][0] = temp[1][i][0]
				dice[0][i][0] = temp[4][i][0]

				
	# R
	elif face[name]==3:
		if dirs =='+':
			for i in range(3):
				dice[1][i][-1] = temp[0][i][-1]
				dice[4][i][-1] = temp[5][i][-1]
				dice[5][i][-1] = temp[1][i][-1]
				dice[0][i][-1] = temp[4][i][-1]	
		else : 
			for i in range(3):
				dice[1][i][-1] = temp[5][i][-1]
				dice[4][i][-1] = temp[0][i][-1]
				dice[5][i][-1] = temp[4][i][-1]
				dice[0][i][-1] = temp[1][i][-1]
	# F
	elif face[name]==4:
		if dirs =='+':
			for i in range(3):
				dice[0][-1][i] = temp[2][-1][i]
				dice[3][-1][i] = temp[0][-1][i]
				dice[5][0][i] = temp[3][-1][2-i]
				dice[2][-1][i] = temp[5][0][2-i]
		else : 
			for i in range(3):
				dice[0][-1][i] = temp[3][-1][i]
				dice[2][-1][i] = temp[0][-1][i]
				dice[5][0][2-i] = temp[2][-1][2-i]
				dice[3][-1][i] = temp[5][0][2-i]
	# D
	elif face[name]==5:
		if dirs =='+':
			for i in range(3):
				dice[2][i][0] = temp[1][0][2-i]
				dice[4][-1][i] = temp[2][i][0]
				dice[3][i][-1] = temp[4][-1][2-i]
				dice[1][0][i] = temp[3][i][-1]
		else : 
			for i in range(3):
				dice[2][i][0] = temp[4][-1][i]
				dice[4][-1][i] = temp[3][2-i][-1]
				dice[3][i][-1] = temp[1][0][i]
				dice[1][0][i] = temp[2][i][0]

	return dice


init_dice =  [[[['w',i*3+j] for j in range(3)] for i in range(3)],
			[[['o',i*3+j] for j in range(3)] for i in range(3)],
			[[['g',i*3+j] for j in range(3)] for i in range(3)],
			[[['b',i*3+j] for j in range(3)] for i in range(3)],
			[[['r',i*3+j] for j in range(3)] for i in range(3)],
			[[['y',i*3+j] for j in range(3)] for i in range(3)]]
face = {'U':0,'B':1,'L':2,'R':3,'F':4,'D':5}
test_case = int(input())
for t in range(test_case):
	n = int(input())
	methods = list(map(str, input().split()))
	dice = copy.deepcopy(init_dice)
	for method in methods:
		dice = rotation(dice, method[0], method[1])
	for i in range(3):
		ans =''
		for j in range(3):
			ans+=dice[0][i][j][0]
		print(ans)