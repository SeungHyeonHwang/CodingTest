
"""
연구소 3
완전탐색 + BFS

활성화 하지 않은 바이러스 
31~36 line 이 핵심.
빈공간이 아니면 복제 시간을 카운트 하지 않음. 
"""

from itertools import combinations
from collections import deque
import copy

def bfs(n,com_virus,space):
	visited = [[-1]*n for _ in range(n)]
	max_time = 0
	q = deque()
	for v in com_virus:
		q.append(v)
		visited[v[0]][v[1]] = 0
	while q : 
		p = q.popleft()
		for i in range(4):
			nx = p[0] + dx[i]
			ny = p[1] + dy[i]
			
			if nx<0 or ny<0 or nx>=n or ny>=n:
				continue
			if maps[nx][ny] == 1 : # 벽이면
				continue
			if visited[nx][ny] == -1  : # 방문하지 않았으면		
				visited[nx][ny] = visited[p[0]][p[1]] + 1
				q.append([nx,ny])
				if maps[nx][ny] == 0 :
					space-=1
					max_time = max(max_time, visited[nx][ny])
			
	if not space : 
		return max_time
	else :
		return int(1e9)


def solution(n,m,space) :
	inf = int(1e9)
	answer = inf
	for com_virus in combinations(virus, m):
		answer = min(bfs(n,com_virus,space), answer)
		#print(answer)
	return answer if answer < inf else -1
	

dx = [-1,0,1,0]
dy = [0,1,0,-1]

n,m = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
virus = []
space = 0
for i in range(n):
	for j in range(n):
		if maps[i][j] == 2 : 
			virus.append([i,j])
		if not maps[i][j] : 
			space+=1
print(solution(n,m,space))