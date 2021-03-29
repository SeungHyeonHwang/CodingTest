
from collections import deque
def cluster(mineral):
	q = deque()
	lst = []
	visited = [[0]*c for _ in range(r)]
	q.append(mineral)
	lst.append(mineral)
	visited[mineral[0]][mineral[1]] = 1
	cnt = 1
	while q :
		p = q.popleft()
		for i in range(4):
			nx = p[0]+dx[i]
			ny = p[1]+dy[i]
			if 0<=nx<r and 0<=ny<c and not visited[nx][ny] and maps[nx][ny]=='.':
				q.append([nx,ny])
				visited[nx][ny] = 1
				lst.append([nx,ny])
				cnt+=1
	if cnt == len(minerals):
		return []
	return lst

dx = [-1,0,1,0]
dy = [0,1,0,-1]
def solution(r,c,n):

	for i in range(n):
		# 왼쪽에서
		if i%2 == 1:
			x,y = r-h[i], c-1
			stop_p = 0
			while True : 
				y-=1
				if y<c :
					break
				elif maps[x][y] == 'x':
					maps[x][y] = '.'
					stop_p = y
					break
			for mineral in minerals:
				if x < mineral[0] and y == mineral[1]:
					lst = cluster(mineral)	
					if not lst :
						lst.sort(key=lambda x:(-x[0],x[1]))
						for l in range(len(lst)) :
							maps[lst[l][0]+1][lst[l][1]] = 'x'
							maps[lst[l][0]][lst[l][1]] = '.'
		elif i%2 == 0 :
			x,y = r-h[i], 0
			stop_p = 0
			while True :
				y+=1
				if y>=c :
					break
				elif maps[x][y] == 'x':
					maps[x][y] = '.'
					stop_p = y
					break
			# 떨어질 미네랄 있는지 확인
			for mineral in minerals:
				if x < mineral[0] and y == mineral[1]:
					lst = cluster(mineral)	
					if not lst :
						lst.sort(key=lambda x:(-x[0],x[1]))
						for l in range(len(lst)) :
							maps[lst[l][0]+1][lst[l][1]] = 'x'
							maps[lst[l][0]][lst[l][1]] = '.'
		

	for i in range(r):
		print(''.join(maps[i]))		
	return 

r,c = map(int, input().split())
maps = [list(map(str, input())) for _ in range(r)]
n = int(input())
h = list(map(int, input().split()))
solution(r,c,n)