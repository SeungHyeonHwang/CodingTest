
"""
 0  1  2  3  4 
 5  6  7  8  9
10 11 12 13 14
15 16 17 18 19
20 21 22 23 24
"""

from itertools import combinations 
from collections import deque

def bfs(comb):

	global answer
	visited = [[0]*5 for _ in range(5)]
	yn,cnt = 0,0

	for c in comb:
		x = int(c/5)
		y = c%5
		visited[x][y] = 1
		yn += 1 if student[x][y] =='Y' else 0
		if yn > 3:
			return

	q = deque()
	q.append(comb[0])
	cnt+=1
	visited[int(comb[0]/5)][comb[0]%5] = 2
	while q :
		p=q.popleft()
		x = int(p/5)
		y = p%5
		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]
			if 0<=nx<5 and 0<=ny<5 :
				if visited[nx][ny] == 1: 
					visited[nx][ny] = 2
					q.append(label[nx][ny])
					cnt+=1
	if cnt == 7:
		answer += 1
		return

def solution():
	global answer
	for comb in combinations([i for i in range(25)], 7):
		bfs(list(comb))
	return answer

dx = [-1,0,1,0]
dy = [0,1,0,-1]
answer = 0 
student = [list(input()) for _ in range(5)]
label = [[i+j*5 for i in range(5)] for j in range(5)]


print(solution())