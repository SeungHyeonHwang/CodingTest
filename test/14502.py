


def get_area(n,m):
	answer = 0
	for comb in combinations(space, 3):
		maps = copy.deepcopy(inst)
		visited = [[0]*m for _ in range(n)]
		spaceArea = len(space)-3
		q = deque()
		for c in comb:
			maps[c[0]][c[1]]=1
			visited[c[0]][c[1]]=1
		for v in virus:
			q.append((v[0],v[1]))
			visited[v[0]][v[1]] = 1 	
			while q :
				x,y = q.popleft()
				for i in range(4):
					nx,ny=x+dx[i],y+dy[i]
					if 0>nx or 0>ny or nx>=n or ny>=m :
						continue
					if visited[nx][ny] or maps[nx][ny]!=0:
						continue
					q.append((nx,ny))
					visited[nx][ny] = 1
					spaceArea-=1
		answer = max(answer, spaceArea)
	return answer 

import copy
from collections import deque
from itertools import combinations
n,m=map(int, input().split())
inst = [list(map(int, input().split())) for _ in range(n)]
space, virus = [], []
dx = [0,1,-1,0]
dy = [-1,0,0,1]
for i in range(n):
	for j in range(m):
		if inst[i][j]==2:
			virus.append((i,j))
		elif inst[i][j]==0:
			space.append((i,j))
print(get_area(n,m))