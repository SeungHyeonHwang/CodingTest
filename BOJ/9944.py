def move(visited, p, d, num, result):
	global answer
	if result > int(1e6):
		return
	if num == 0 :
		answer = min(answer, result)
		return
	
	nx,ny = p[0]+dx[d], p[1]+dy[d]
	if 0<=nx<n and 0<=ny<m and maps[nx][ny]=='.' and not visited[nx][ny] : 
		visited[nx][ny] = 1	
		move(visited,[nx,ny],d,num-1,result)
		visited[nx][ny] = 0 
		return
	for i in range(4):
		if i!=d :
			nx,ny = p[0]+dx[i], p[1]+dy[i]
			if nx<0 or ny<0 or nx>=n or ny>=m:
				continue
			if maps[nx][ny]=='*' or visited[nx][ny] : 
				continue
			visited[nx][ny] = 1
			move(visited,[nx,ny],i,num-1,result+1)
			visited[nx][ny] = 0 
	return

def solution(n,m):
	global answer
	start_points = [[i,j] for i in range(n) for j in range(m) if maps[i][j]=='.']
	num = len(start_points)
	for p in start_points:
		for d in range(4):
			visited = [[0]*m for _ in range(n)]
			visited[p[0]][p[1]]=1
			move(visited, p, d, num-1, 1)
			visited[p[0]][p[1]]=0
	return answer if answer < int(1e6) else -1



dx = [-1,0,1,0]
dy = [0,-1,0,1]
case = 1
while True : 
	try : 
		answer = int(1e6)
		n,m = map(int, input().split())
		maps = [list(map(str, input())) for _ in range(n)]
		print('Case %d: %d'%(case, solution(n,m)))
		case+=1
	except EOFError:
		break