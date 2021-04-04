"""
구슬탈출 2
골 2 
<구조>
1) bfs
2) visited : rx,ry,bx,by의 위치 조합이 같은 경우 배제
3) move + cnt : while문 활용과 동시에 cnt로 이동 거리 카운트

"""


def move(x,y,i):
	cnt = 0 
	#현재위치가 O거나 다음 위치가 벽이면 멈춤
	while maps[x+dx[i]][y+dy[i]]!='#'and maps[x][y]!='O':
		x+=dx[i]
		y+=dy[i]
		cnt+=1
	return x,y,cnt

from collections import deque

def bfs():
	global answer
	q = deque()
	q.append((R[0],R[1],B[0],B[1],1))
	visited[R[0]][R[1]][B[0]][B[1]] = True

	while q : 
		rx,ry,bx,by,depth = q.popleft()
		if depth > 10 : return 
		for i in range(4):
			nrx,nry,rcnt = move(rx,ry,i)
			nbx,nby,bcnt = move(bx,by,i)

			if maps[nbx][nby] =='O':
				continue
			if maps[nrx][nry] =='O':
				answer = depth
				return
			if nrx==nbx and nry==nby : 
				if rcnt > bcnt : 
					nrx-=dx[i]
					nry-=dy[i]
				else :
					nbx-=dx[i]
					nby-=dy[i]
			if not visited[nrx][nry][nbx][nby] : 
				q.append((nrx,nry,nbx,nby,depth+1))
				visited[nrx][nry][nbx][nby] = True

	return
answer = -1
dx = [-1,0,1,0]
dy = [0,-1,0,1]
n,m = map(int, input().split())
maps = [list(map(str, input())) for _ in range(n)]
R,B,O = [],[],[]
visited = [[[[False]*m for _ in range(n)] for _ in range(m)] for _ in range(n)]
for i in range(n):
	for j in range(m):
		if maps[i][j]=='R': R = [i,j]
		elif maps[i][j]=='B': B = [i,j]
		elif maps[i][j]=='O': O = [i,j]
bfs()
print(answer)