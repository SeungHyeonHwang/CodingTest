







import copy
from collections import deque
from itertools import combinations

def bfs(virus, wall, maps) : 

	maps = copy.deepcopy(maps2)
	q = deque()

	for w in wall : 
		maps[w[0]][w[1]] = 1
	for v in virus:
		q.append(v)
	while q :
		x,y = q.popleft()
		for i in range(4): 
			nx = x + dx[i]
			ny = y + dy[i]

			if nx >= N or nx < 0 or ny >= M or ny < 0 :
				continue
			if maps[nx][ny] != 0 :
				continue
			q.append([nx,ny])
			maps[nx][ny] = 2
	# 안전영역 크기
	safe_area = 0
	for i in range(N) :
		for num in sorted(maps[i]):
			if num > 0 :
				break
			else : 
				safe_area +=1
	return safe_area

if __name__ == '__main__':
	answer=0

	N, M = map(int, input().split())
	maps2 = [list(map(int, input().split())) for _ in range(N)]
	candidate = []
	virus = []
	for i in range(N):
		for j in range(M):
			if maps2[i][j] == 2 : 
				virus.append([i,j])
			elif maps2[i][j] == 0 :
				candidate.append([i,j])
	dx = [-1,0,1,0]
	dy = [0,1,0,-1]

	for wall in list(combinations(candidate, 3)) : 
		answer = max(answer, bfs(virus, wall, maps2))
	print(answer)