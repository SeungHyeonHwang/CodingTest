"""
미로 탈출
처음에 재귀로 풀었는데 최대 recursion error 발생
반복문으로 수정하여 해결

"""

#  x 0 1 o
# -1 0 1 2

def escape(i,j,trace):

	while True : 
		visited[i][j] = 2
		trace.append([i,j])
		if maze[i][j] == 'U':
			nx,ny = i-1,j
		elif maze[i][j] =='R':
			nx,ny = i,j+1
		elif maze[i][j] == 'D':
			nx,ny = i+1,j
		elif maze[i][j] == 'L':
			nx,ny = i,j-1
		
		if nx<0 or ny<0 or nx>=n or ny>=m:
			trace.insert(0,True)
			break
		if visited[nx][ny] == 0 or visited[nx][ny] == 2 : 
			trace.insert(0,False)
			break
		elif visited[nx][ny] == 1 :
			trace.insert(0,True)
			break
		
		i,j = nx,ny
	return trace


def solution(n,m):
	global answer

	for i in range(n):
		for j in range(m):
			if visited[i][j] == 0 :
				continue
			if visited[i][j] == 1 : 
				answer+=1
			elif visited[i][j] == -1 : 
				trace = escape(i,j,[]) 
				if trace[0] :
					answer+=1
					for t in trace[1:] : 
						visited[t[0]][t[1]] = 1
				else :
					for t in trace[1:] : 
						visited[t[0]][t[1]] = 0

	return answer
answer = 0 
n,m = map(int, input().split())
maze = [list(map(str, input())) for _ in range(n)]
visited = [[-1]*m for _ in range(n)]
print(solution(n,m))