



import math
def firestorm(fire) :
	global ans1, ans2
	temp_map = [[0]*2**n for _ in range(2**n)]

	grid = (2**n * 2**n) // ((fire+1) * (fire+1))
	#print(grid, (2**n * 2**n), int(math.sqrt(grid)), ((fire+1) * (fire+1)), 2**fire)

	fy = [x for x in range(0, len(temp_map[0]), int(2**(fire)))] 
	fx = [x for x in range(0, len(temp_map[0]), int(2**(fire)))]
	
	print(fx, fy)
	print()
	for i in range(2**n) : 
		print(maps[i])
	print()
	# 격자 수
	c = 0 
	for g1 in range(len(fx)) : 

		for g2 in range(len(fy)) : 

			x, y = fx[g1], fy[g2]
			print(x,y)
			# 각 격자
			
			#회전
			#for c in range(4):
			for i in range(2**fire) : 
				for j in range(2**fire) : 
					
					print(x+i, y+j, '->', x+i+(fire+1)*dx[c], y+j+(fire+1)*dy[c])
					temp_map[x+i+(fire+1)*dx[c]][y+j+(fire+1)*dy[c]] = maps[x+i][y+j]
			c = (c+1)%4

	for i in range(2**n) : 
		print(temp_map[i])
	print()



	return ans1, ans2

if __name__ == "__main__" : 
	
	file = open('ex1.txt')
	for i,line in enumerate(file) : 
		if i == 0 : 
			n,q = map(int, line.split())
			maps = [[] for _ in range(2**n)]
			fires = []
		elif i <= 2**n : maps[i-1] = list(map(int, line.split()))
		else : fires = list(map(int, line.split()))
	
	# 시계방향
	dx = [0,1,0,-1]
	dy = [1,0,-1,0]
	ans1, ans2 = 0,0
	for fire in fires : 
		firestorm(fire)
	print(ans1)
	print(ans2)
