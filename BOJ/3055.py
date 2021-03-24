

from collections import deque

def bfs_water(water) : 
	for i in range(len(water)) : 
		p = water.popleft()
		for j in range(4):
			nx = p[0] + dx[j]
			ny = p[1] + dy[j]
			if 0>nx or 0>ny or r<=nx or c<=ny : 
				continue
			if maps[nx][ny] == '*' or maps[nx][ny] == 'X' or maps[nx][ny] =='D':
				continue
			maps[nx][ny] = '*'
			water.append([nx,ny])

def bfs_kak(kak) : 
	global answer
	for i in range(len(kak)) : 
		p = kak.popleft()
		if maps[p[0]][p[1]] == '*':
			continue
		for i in range(4):
			nx = p[0] + dx[i]
			ny = p[1] + dy[i]
			if 0>nx or 0>ny or r<=nx or c<=ny : 
				continue
			if maps[nx][ny] == '*' or maps[nx][ny] == 'X':
				continue
			if visited[nx][ny] : 
				continue
			if maps[nx][ny] =='D':
				answer =  visited[p[0]][p[1]]
				kak.append([nx,ny])
				break
			kak.append([nx,ny])
			visited[nx][ny] = visited[p[0]][p[1]] + 1

	

def solution(r,c) : 
	global answer
	while True : 
		if end in kak : 
			return answer
		if not kak : 
			return "KAKTUS"
		bfs_kak(kak) 
		bfs_water(water)



r,c = map(int, input().split())
maps = [list(map(str, input())) for _ in range(r)]
answer = 0 
dx = [1,0,-1,0]
dy = [0,1,0,-1]
kak, water = deque(),deque()
end = []
visited = [[0]*c for _ in range(r)]
for i in range(r):
	for j in range(c):
		if maps[i][j] == 'S':
			kak.append([i,j])
			visited[i][j] = 1
		elif maps[i][j] == '*':
			water.append([i,j])
		elif maps[i][j] == 'D':
			end = [i,j]
print(solution(r,c))