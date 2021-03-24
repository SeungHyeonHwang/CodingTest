


import itertools
from collections import deque

def bfs(w,h,numbers) : 
	global dx, dy

	bricks = [[0]*h for _ in range(w)]
	for i in range(w):
		for j in range(h):
			bricks[i][j] = maps[j][i]

	for num in numbers : 
		x = 0
		# 블록이 있을때까지 내려감 
		while not bricks[num][x] :
			x+=1
			if x >= h-1 :
				break
		# 벽돌 파괴
		q = deque()
		q.append([num,x])

		while q : 
			y,x = q.popleft()
		
			bsize = bricks[y][x]
			bricks[y][x] = 0 # 중복방지
			# 크기-1만큼 퍼져나감
			for i in range(bsize-1):
				# 4방향
				for j in range(4):
					nx = x+(i+1)*dx[j]
					ny = y+(i+1)*dy[j]
					if 0<=nx<h and 0<=ny<w:
						if bricks[ny][nx] == 0:
							continue	
						q.append([ny,nx])

		for i in range(w):
			delState=False
			for j in range(h):
				if bricks[i][j] :
					delState = True
				elif delState and bricks[i][j] == 0 : 
					bricks[i].pop(j)
					bricks[i].insert(0,0)

	# 남아있는 블럭 수 
	temp=0
	for i in range(w):
		temp+=bricks[i].count(0)

	return w*h-temp

def solution(n,w,h):
	ans = 1e9

	l = [i for i in range(w)]
	for numbers in itertools.product(l, repeat=n):
		ans = min(ans, bfs(w,h,list(numbers)))
		if ans == 0 :
			return ans
	return ans

dx = [0,-1,0,1]
dy = [-1,0,1,0]
"""
file = open("ex1.txt")
for i,f in enumerate(file) :
	if i == 0:
		n,w,h = map(int, f.split())
		maps = [[] for _ in range(h)]
	else : 
		maps[i-1] = list(map(int, f.split()))
"""
n,w,h = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(h)]
print(solution(n,w,h))