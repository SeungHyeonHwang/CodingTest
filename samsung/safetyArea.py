
from collections import deque
def bfs(h, p, visited):
	q = deque()
	q.append(p)
	visited[p[0]][p[1]] = 1
	while q : 
		v = q.popleft()
		for i in range(4):
			nx = v[0] + dx[i]
			ny = v[1] + dy[i]
			if 0 > nx or 0 > ny or nx >= n or ny >= n :
				continue
			if visited[nx][ny] :
				continue
			if maps[nx][ny] > h :
				q.append((nx,ny))
				visited[nx][ny] = 1
	return 1

def solution(n):
	answer = 1
	for h in range(101):
		result = 0
		safetyPoint = []
		visited = [[0]*n for _ in range(n)]		

		for i in range(n):
			for j in range(n):
				if maps[i][j] > h:
					safetyPoint.append((i,j))
		for p in safetyPoint : 
			if not visited[p[0]][p[1]] :
				result+=bfs(h, p, visited)

		answer = max(result, answer)

	return answer

dx = [-1,0,1,0]
dy = [0,1,0,-1]
n = int(input())
maps = [list(map(int, input().split())) for _ in range(n)]
print(solution(n))