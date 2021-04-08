

n = int(input())
tiles = [[] for _ in range(n)]
for i in range(n):
	if i%2==0:
		for j in range(n):
			tiles[i].extend(list(map(int, input().split())))
	else :
		temp = [0]
		for j in range(n-1):
			temp.extend(list(map(int, input().split())))
			tiles[i] = temp
		temp.append(0)

checked = [[0]*n*2 for _ in range(n)]
for i in range(n):
	for j in range(1, 2*n-1):
		if tiles[i][j] == tiles[i][j-1]:
			checked[i][j] = 1
			checked[i][j-1] = 1

for i in range(1,2*n-1):
	for j in range(1,n):
		if tiles[j][i] == tiles[j-1][i]:
			checked[j][i] = 1
			checked[j-1][i] = 1


dx = [-1,0,1,0]
dy = [0,-1,0,1]

checked[0][0] = 2
answer = 0 
def dfs(p, n, result):
	if p[0] == n-1 and p[1] == 2*n-2:
		answer = checked[p[0]][p[1]]-1
		return
	for i in range(4):
		nx, ny = p[0]+dx[i], p[1]+dy[i]
		if 0<=nx<n and 0<=ny<n*2 and checked[nx][ny] == 1 : 
			if p[0]!=nx:  checked[nx][ny] = checked[p[0]][p[1]]+1
			elif p[0]%2==0 and p[1]//2 == ny//2 :
				checked[nx][ny] = checked[p[0]][p[1]] 
			elif p[0]%2==1 and (p[1]-1)//2 == (ny-1)//2 :
				checked[nx][ny] = checked[p[0]][p[1]] 
			else : 
				checked[nx][ny] = checked[p[0]][p[1]]+1
			dfs((nx,ny), n, result)
dfs((0,0),n,[])
for i in range(n):
	print(checked[i])
print()		
print(answer)