# amount 하나 때문에 틀렸던 문제
# 기존 큐에 저장된 값을 통해 다음값 업데이트 해야함

from collections import deque

def solution(board):
	answer = int(10e9)
	n = len(board[0])
	# 남 동 북 서
	dx = [1,0,-1,0]
	dy = [0,1,0,-1]
	
	visited = [[0]*n for _ in range(n)]
	q = deque()
	q.append([0,0,-1,0])
	end = [n-1, n-1]
	visited[0][0] = 1

	while q : 
		p = q.popleft()
		x,y,d,amount = p[0], p[1], p[2], p[3]
		for i in range(4): 
			nx, ny = x+dx[i], y+dy[i]
			if 0<=nx<n and 0<=ny<n and board[nx][ny] == 0 :
				if visited[nx][ny] == 0 :
					if (i-d)%2 != 0 and d >= 0 :
						visited[nx][ny] = amount + 600
					else : 
						visited[nx][ny] = amount + 100
					q.append([nx,ny,i,visited[nx][ny]])

				else :
					if (i-d)%2 != 0 and d >= 0 :
						if visited[nx][ny] >= amount + 600 :
							visited[nx][ny] = amount + 600
							q.append([nx,ny,i,visited[nx][ny]])
					else : 
						if visited[nx][ny] >= amount + 100 : 
							visited[nx][ny] = amount + 100
							q.append([nx,ny,i,visited[nx][ny]])

				if nx == end[0] and ny == end[1] :
					answer = min(answer, visited[nx][ny])

	return answer

		



board = [[0,0,0,0],[0,1,0,0],[0,0,0,0],[0,0,0,0]]
board = [[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]
#board = [[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]]
#board = [[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]]	
print(solution(board))