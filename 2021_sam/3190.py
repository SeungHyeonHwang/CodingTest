"""
다시 풀기 
이동이 아니라 꼬리제거 개념....
뱀이 아니라 머리만 신경쓴 visited 개념....
"""
from collections import deque

def rotation(d, c):
	if c == "L":
		d=(d-1)%4
	else :
		d=(d+1)%4
	return d


n = int(input())
k = int(input())
maps = [[0]*n for _ in range(n)]
for _ in range(k):	
	x,y = map(int, input().split())
	maps[x-1][y-1] = 1

dir_dict = dict()
l = int(input())
for i in range(l):
	t, d = input().split()
	dir_dict[int(t)] = d

dx = [0,1,0,-1]
dy = [1,0,-1,0]


visited = deque([[0,0]])
maps[0][0] = 2
game_time = 1
d = 0
x,y = 0,0

while True : 
	x = x+dx[d]
	y = y+dy[d]
	
	if 0<=x<n and 0<=y<n and maps[x][y]!=2: 
		
		if maps[x][y] == 0 :
			temp_x, temp_y = visited.popleft()
			maps[temp_x][temp_y] = 0
		maps[x][y] = 2
		visited.append([x,y])
		if game_time in dir_dict.keys():
			d = rotation(d, dir_dict[game_time])
		game_time+=1
	else : 
		print(game_time)
		break
