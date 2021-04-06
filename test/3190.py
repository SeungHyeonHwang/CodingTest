"""
뱀 
골 5

x,y로 머리 정보 이용
q는 꼬리 제거용 
새로 append 된 nx,ny 는 새 머리 정보
다음에 q.popleft는 꼬리가 삭제됨 ( 선입 선출 )
"""

n = int(input())
k = int(input())
apples = [list(map(int, input().split())) for _ in range(k)]
l = int(input())
directions = [list(map(str, input().split())) for _ in range(l)]
maps = [[0]*n for _ in range(n)]
dx=[0,1,0,-1]
dy=[1,0,-1,0]
for apple in apples : 
	maps[apple[0]-1][apple[1]-1] = 1

from collections import deque

def play():
	answer = 0
	q = deque()
	q.append((0,0))
	x,y,d,cnt=0,0,0,0 # 머리 정보
	maps[x][y] = 2
	while True :
		nx,ny = x+dx[d],y+dy[d]
		answer+=1
		if 0>nx or 0>ny or nx>=n or ny>=n or maps[nx][ny]==2:
			return answer
		if not maps[nx][ny] : 
			tx,ty = q.popleft()
			maps[tx][ty]=0
		q.append((nx,ny))
		maps[nx][ny]=2
		x,y = nx,ny
		if cnt<len(directions) and int(directions[cnt][0])==answer:
			
			if directions[cnt][1]=='D': d=(d+1)%4
			else : d=(d-1)%4
			cnt+=1

print(play())