"""
로봇 청소기
골 5
"""
def clean(x,y,d,answer):
	while True: 
		flag = False
		for i in range(4):
			# 현재기준 왼쪽부터
			nd = (d-1)%4 
			nx,ny = x+dx[nd], y+dy[nd]
			d=nd
			# 청소하지 않았다면
			if not maps[nx][ny]: 
				maps[nx][ny]=2
				answer+=1
				x,y=nx,ny
				flag = True
				break
		if not flag: # 4방향 청소할 곳 없다면
			# 후진할 수 없으면
			if maps[x-dx[d]][y-dy[d]]==1: 
				return answer
			x,y = x-dx[d],y-dy[d]

n,m=map(int, input().split())
x,y,d = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
dx = [-1,0,1,0] # 북동남서
dy = [0,1,0,-1]
maps[x][y]=2 # 현재 청소, answer은 1 부터 시작
print(clean(x,y,d,1))