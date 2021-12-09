n = int(input())
data = [list(map(int, input().split())) for _ in range(n*n)]
maps = [[0]*3]*3
maps[1][1] = data[0][0]

x = [-1,1,0,0]
y = [0,0,1,-1]
oneStatus = False
secondStatus = False
for i in range(1,len(data)):
	student = data[i][0]
	love = data[i][1:]

	temp_maps = [[0]*3]*3
	max_num = 0
	for j in range(n):
		for k in range(n):
			for h in range(4):
				if j+x < n and j+x > 0 and y+k < n and y+k > 0 :
					# 좋아하는 학생 있으면 
					if maps[j+x][k+y] in love : 
						temp_maps[j+x][k+y]+=1
						max_num = max(max_num, temp_maps[j+x][k+y])
						oneStatus = True
	if oneStatus : 
		for j in range(n):
			for k in range(n):
				if temp_maps[j][k] == max_num : 
					maps[j][k] = student
 




