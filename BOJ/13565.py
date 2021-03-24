# 침투
# dfs/bfs

from collections import deque
def bfs(start, maxDepth):
	q = deque()
	for s in start:
		q.append(s)
		visited[s[0]][s[1]] = 1 
	while q :
		p = q.popleft()
		for i in range(4):
			nx = p[0] + dx[i]
			ny = p[1] + dy[i]
			if nx<0 or ny<0 or nx>=n or ny>=m:
				continue
			if visited[nx][ny] or mat[nx][ny] :
				continue
			q.append((nx,ny))
			visited[nx][ny] = 1
			if maxDepth < nx : 
				maxDepth = nx
	return maxDepth

def solution(n,m):
	start = [(0,j) for j in range(m) if mat[0][j] == 0]
	maxDepth = 0
	maxDepth = bfs(start, maxDepth)
	return "YES" if maxDepth == n-1  else "NO"


dx = [-1,0,1,0]
dy = [0,1,0,-1]
n,m = map(int, input().split())
mat = [list(map(int, input())) for _ in range(n)] 
visited = [[0]*m for _ in range(n)]
print(solution(n,m))