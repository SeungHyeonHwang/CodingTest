
def rotation(d) :
	if d == 0 : return 3 
	else : return d-1

def dfs(x,y,d) :
	global answer
	# 현재 위치 청소
	if maps[x][y] == 0 :
		maps[x][y] = 2
		answer +=1

	for i in range(4) : 
		nd = rotation(d) # 현재 방향에서 왼쪽 
		nx = x + dx[nd]
		ny = y + dy[nd]

		# a
		if maps[nx][ny] == 0 : 
			dfs(nx,ny,nd)
			return
		d = nd

	nd = rotation(rotation(d))
	x+=dx[nd]
	y+=dy[nd]

	if maps[x][y] == 1:
		return
	dfs(x,y,d)	

		
if __name__ == '__main__' : 

	N,M = map(int, input().split())
	x,y,d = map(int, input().split())
	maps = [list(map(int, input().split())) for _ in range(N)]
	answer = 0 
	dx = [-1,0,1,0] # 북동남서
	dy = [0,1,0,-1]
	dfs(x,y,d)
	print(answer)
