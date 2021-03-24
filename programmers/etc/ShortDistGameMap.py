# https://programmers.co.kr/learn/courses/30/lessons/1844
# 게임맵최단거리 

from collections import deque
def solution(maps):
	answer = 0
	n = len(maps)
	m = len(maps[0])
	dx = [-1,0,1,0]
	dy = [0,1,0,-1]

	q = deque()
	q.append((0,0))
	visited = [[0]*m for _ in range(n)]
	visited[0][0] = 1
	
	while q :
		p = q.popleft()
		for i in range(4):
			nx = p[0]+dx[i]
			ny = p[1]+dy[i]
			if 0<=nx<n and 0<=ny<m and not visited[nx][ny] and maps[nx][ny] :
				maps[nx][ny] = maps[p[0]][p[1]] + 1
				q.append((nx,ny))
				visited[nx][ny] = 1
			if nx==n-1 and ny == m-1:
				return maps[nx][ny]
	return -1

maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]
print(solution(maps))