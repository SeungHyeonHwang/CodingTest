# 연구소

from itertools import permutations 
from collections import deque
def dfs(v):
	q = deque()
	q.append(v)
	

n,m = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]

wall_cand = []
for i in range(n):
	for j in range(n):
		if maps[i][j] == 1 :
			wall_cand.append([i,j])
		if maps[i][j] == 0 :
			virus.append([i,j])

for cands in permutations(wall_cand, 3):
	temp = maps[:]
	for cand in cands : 
		temp[cand[0]][cand[1]] = 1
	
	for v in virus : 
		visited = [[0 for _ in range(n)] for _ in range(n)]
		dfs(v, visited)