"""
마법사 상어와 파이어 볼
4 2 1
1 1 5 2 2
1 4 7 1 6
"""


def solution(N,M,K):

	answer = 0
	
	for k in range(K):
		# 1. 
		temp = []
		for i in range(len(q)):
			x,y = q.popleft()
			for _ in range(len(maps[x][y])):
				m,s,d = maps[x][y].popleft()
				nx,ny = x+dx[d]*s, y+dy[d]*s
				if nx < 0 : nx = N-1+nx+1
				if ny < 0 : ny = N-1+ny+1
				if nx >= N : nx%=N
				if ny >= N : ny%=N
				temp.append([nx,ny,m,s,d])
				q.append([nx,ny])
		for x,y,m,s,d in temp : 
			maps[x][y].append([m,s,d])
		# 2.

		for i in range(N):
			for j in range(N):
				num = len(maps[i][j])
				if num > 1 : 
					me = maps[i][j][0][0]
					sp = maps[i][j][0][1]
					di = maps[i][j][0][2]%2
					st = True
					for l in range(1,num):
						me+=maps[i][j][l][0]
						sp+=maps[i][j][l][1]
						if di != maps[i][j][l][2]%2 : 
							st = False
					me=int(me/5)
					# 3. 
					if me :
						sp = int(sp/num)
						nd = [0,2,4,6] if st else [1,3,5,7]
						# 2. 
						for o in range(4):
							nx = i+dx[nd[o]]
							ny = j+dy[nd[o]]
							if nx < 0 : nx = N-1+nx+1
							if ny < 0 : ny = N-1+ny+1
							if nx >= N : nx%=N
							if ny >= N : ny%=N
							maps[nx][ny].append([me,sp,nd[o]])
	for i in range(N):
		print(maps[i])

	for i in range(N):
		for j in range(N):
			if maps[i][j]:
				for m,s,d in maps[i][j] : 
					answer += m 

"""
check
"""

	return answer

from collections import deque
N,M,K = map(int, input().split())
maps = [[deque() for _ in range(N)] for _ in range(N)]
q = deque()
dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,1,1,1,0,-1,-1,-1]
for _ in range(M):
	r,c,m,s,d = map(int, input().split())
	maps[r-1][c-1].append([m,s,d])
	q.append([r-1,c-1])
print(solution(N,M,K))
