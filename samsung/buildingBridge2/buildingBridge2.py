from collections import deque
def isBoundary(p):
	for i in range(4):
		nx = p[0]+dx[i]
		ny = p[1]+dy[i]
		if nx < 0 or ny < 0 or nx >= n or ny >= m :
			continue
		if not maps[nx][ny] :
			return True
	return False

def bfs(idx,p):
	global n,m
	q = deque()
	arr = []
	q.append(p)
	if isBoundary(p):
		arr.append([p[0],p[1]])
	visited[p[0]][p[1]] = 1
	maps[p[0]][p[1]] = idx
	while q :
		x,y = q.popleft()
		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]
			if nx < 0 or ny < 0 or nx >= n or ny >= m :
				continue
			if visited[nx][ny] :
				continue
			if maps[nx][ny] : 
				maps[nx][ny] = idx
				visited[nx][ny] = 1
				q.append([nx,ny])
				if isBoundary([nx,ny]):
					arr.append([nx,ny])
	return arr

def solution(n,m):
	answer = 0
	for i in range(len(lands)):
		for k in range(len(lands)): # 나머지
			# 자기 자신 아니면
			if i != k :
				for p1 in lands[i] : 
					for p2 in lands[k]:

						if p1[0] == p2[0] : 
							# 중간에 1이 없어야함
							length = 0
							a,b=p1[1], p2[1]
							if p1[1] > p2[1] : a,b = b,a
							for j in range(a+1, b+1):
								if maps[p1[0]][j] : 
									if maps[p1[0]][j] != maps[p1[0]][p1[1]] and maps[p1[0]][j] != maps[p2[0]][p2[1]]:
										length = 0
									break
								else : 
									length+=1
							if length > 1 : 
						
								bridges[i][k] = min(bridges[i][k], length)

						if p1[1] == p2[1] : 
							length = 0
							a,b=p1[0], p2[0]
							if p1[0] > p2[0] : a,b = b,a
							for j in range(a+1, b+1):
								if maps[j][p1[1]] :
									if maps[j][p1[1]] != maps[p1[0]][p1[1]] and maps[j][p1[1]] != maps[p2[0]][p2[1]]:
										length = 0
									break
								else : 
									length+=1
							if length > 1 : 
	
								bridges[i][k] = min(bridges[i][k], length)

	new_bridges = []
	for i in range(len(lands)):
		for j in range(len(lands)):
			if bridges[i][j] != 101 : 
				new_bridges.append([i,j,bridges[i][j]])

	parent = [i for i in range(len(lands))]
	new_bridges.sort(key=lambda x:x[-1])
	for item in new_bridges:
		i,j,v = item[0], item[1], item[2]
		if find_parent(parent,i) != find_parent(parent,j):
			answer += v
			union_parent(parent, i, j)

	root = 0
	for i in range(len(lands)):
		if root != find_parent(parent,i):
			return -1
	return answer 

def find_parent(parent,x):
	if parent[x] != x : 
		parent[x] = find_parent(parent, parent[x])
	return parent[x]
def union_parent(parent,a,b):
	a = find_parent(parent,a)
	b = find_parent(parent,b)
	if a < b:
		parent[b] = a
	else :
		parent[a] = b


dx = [-1,0,1,0]
dy = [0,1,0,-1]
n,m = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]

visited = [[0]*m for _ in range(n)]
points = []
for i in range(n):
	for j in range(m):
		if maps[i][j] : 
			points.append([i,j])
lands = []
idx = 1
for p in points : 
	if not visited[p[0]][p[1]]:
		lands.append(bfs(idx,p))
		idx+=1
bridges = [[101]*len(lands) for _ in range(len(lands))]
print(solution(n,m))