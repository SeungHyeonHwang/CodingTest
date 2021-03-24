"""
마법사 상어와 파이어볼 
골5
4 2 1
1 1 5 2 2
1 4 7 1 6
"""


def solution(N,M,K,rcmsd):
	dx = [-1,-1,0,1,1,1,0,-1]
	dy = [0,1,1,1,0,-1,-1,-1]
	answer = 0
	maps = [[[] for _ in range(N)] for _ in range(N)]

	for k in range(K):
		# 1. 파이어볼 이동
		for i in range(M):
			r,c,m,s,d = map(int, rcmsd[i])
			nx,ny = r-1+dx[d]*s, c-1+dy[d]*s
			if nx < 0 : nx = N-1+nx+1
			if ny < 0 : ny = N-1+ny+1
			if nx >= N : nx%=N
			if ny >= N : ny%=N
			maps[nx][ny].append([m,s,d,False])

		# 2. 이동 후 
		rcmsd = []

		for i in range(N):
			for j in range(N):
				num = len(maps[i][j])
				if num==1 and not maps[i][j][-1] :
					rcmsd.append([i,j]+maps[i][j][0])
				elif num > 1 : 
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
					# 3. 파이어볼 합치기
					if me :
						sp = int(sp/num)
						nd = [0,2,4,6] if st else [1,3,5,7]
						# 2. 4개로 나눔
						for o in range(4):
							nx = i+dx[nd[o]]
							ny = j+dy[nd[o]]
							if nx < 0 : nx = N-1+nx+1
							if ny < 0 : ny = N-1+ny+1
							if nx >= N : nx%=N
							if ny >= N : ny%=N
							rcmsd.append([nx,ny,me,sp,nd[o]])
							maps[nx][ny].append([me,sp,nd[o],True])
					# 4. 소멸
					maps[i][j] = []
	for i in range(N):
		print(maps[i])
	print(rcmsd)
	for i in rcmsd : 
		answer+=i[2]

	return answer

N,M,K = map(int, input().split())
RCMSD = [list(map(int, input().split())) for _ in range(M)]
print(solution(N,M,K,RCMSD))
