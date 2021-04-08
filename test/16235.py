
def solution(n,m,k):
	answer = 0
	
	for _ in range(k):
		for i in range(n):
			for j in range(n):
				if ground[i][j] :
					ground[i][j].sort()
					death_tree = 0

					temp_tree = []
					for tree in ground[i][j] : 
						if food[i][j] >= tree :
							food[i][j]-=tree 
							tree+=1
							temp_tree.append(tree)
			
						else : 
							death_tree+=tree//2
					ground[i][j] = []
					ground[i][j].extend(temp_tree)
					food[i][j]+=death_tree


	
		for i in range(n):
			for j in range(n):
				food[i][j]+=s2d2[i][j]
				if ground[i][j]:
					for tree in ground[i][j]:
						if tree%5==0 :
							for d in range(8):
								nx,ny=i+dx[d],j+dy[d]
								if nx<0 or ny<0 or nx>=n or ny>=n:
									continue
								ground[nx][ny].append(1)

	for i in range(n):
		for j in range(n):
			answer+=len(ground[i][j])
	return answer 


dx=[-1,-1,-1,0,1,1,1,0]
dy=[-1,0,1,1,1,0,-1,-1]

n,m,k = map(int, input().split())
s2d2 = [list(map(int, input().split())) for _ in range(n)]
trees = [list(map(int, input().split())) for _ in range(m)]
ground = [[[] for _ in range(n)] for _ in range(n)]
food = [[5]*n for _ in range(n)]
for tree in trees :
	ground[tree[0]-1][tree[1]-1].append(tree[-1])
print(solution(n,m,k))