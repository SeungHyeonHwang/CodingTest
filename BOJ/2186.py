




def dfs(st, comb, cnt, k):

	if cnt >= len(eng) : 
		answer_set.add(comb)
		return
	for i in range(k):
		for j in range(4):
			nx, ny = st[0]+dx[j]*(i+1), st[1]+dy[j]*(i+1)
			if 0<=nx<=n and 0<=ny<m :
				if maps[nx][ny] == eng[cnt]:
					dfs([nx,ny], comb+str(idx_map[nx][ny]), cnt+1, k)
				


dx = [-1,0,1,0]
dy = [0,-1,0,1]
n,m,k = map(int, input().split())
maps = [list(map(str, input())) for _ in range(n)]
eng = list(map(str, input()))
st = [[i,j] for i in range(n) for j in range(m) if maps[i][j]==eng[0]]
idx_map = [[i+j*m for i in range(m)] for j in range(n)] 

answer_set = set()
dfs(st[0],'%s'%str(idx_map[st[0][0]][st[0][1]]),1,k)
print(len(answer_set))