
"""
dfs 로 푸는게 미쳤다 그냥 ...
+ 가지치기 이해가 안됨 ... 
"""

def dfs(i,j,idx,total):
	global max_num
	# 가지치기.. 
	if max_num >= total + max_val * (3 - idx):
		return
	if idx == 3: 
		max_num = max(max_num, total)
		return 
	else : 
		for k in range(4):
			nx = i+dx[k]
			ny = j+dy[k]
			if 0<=nx<n and 0<=ny<m and visited[nx][ny] == 0 :
				if idx == 1 : 
					visited[nx][ny] = 1
					dfs(i,j,idx+1,total+arr[nx][ny])
					visited[nx][ny] = 0
				visited[nx][ny] = 1
				dfs(nx,ny,idx+1,total+arr[nx][ny])
				visited[nx][ny] = 0

n,m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]
dx=[0,-1,0,1]
dy=[1,0,-1,0]
max_num = 0
max_val = max(map(max, arr))
for i in range(n):
	for j in range(m):
		visited[i][j] = 1
		dfs(i,j,0,arr[i][j])
		visited[i][j] = 0
print(max_num)