


from collections import deque

def check(nx,ny):
	for nr in rect : 
		if maps[nx+nr[0]][ny+nr[1]] :
			return False
	return True



def solution(n,m):
	answer = 0
	q = deque()
	q.append([r[2]-1,r[3]-1])
	visited = [[0]*m for _ in range(n)]
	visited[r[2]-1][r[3]-1] = 1
	while q : 
		p = q.popleft()
		if p[0] == r[4]-1 and p[1] == r[5]-1:
			answer = visited[p[0]][p[1]]-1
			break
		for i in range(4):
			nx, ny = p[0]+dx[i], p[1]+dy[i]
			# 맨왼쪽 맨위는 0부터 
			if 0<=nx<=n-r[0] and 0<=ny<=m-r[1] and not visited[nx][ny] and check(nx,ny):
				q.append([nx,ny])
				visited[nx][ny] = visited[p[0]][p[1]]+1
	return answer if answer else -1

dx = [0,-1,0,1]
dy = [1,0,-1,0]
n,m= map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
r = list(map(int, input().split())) # h,w, sr, sc, fr, fc
rect = []

for j in range(r[1]):
	rect.append([0, j])
	rect.append([r[0]-1, j])
for i in range(r[0]):
	rect.append([i, r[1]-1])
	rect.append([i, 0])
print(solution(n,m))