# 참조 : https://jjangsungwon.tistory.com/27 



from collections import deque 

def dfs() :
	global answer
	
	snake = deque()
	
	answer +=1
	x,y,d,cnt = 0,0,1,0
	maps[x][y] = 1
	snake.append([x,y])

	while True : 
		# 머리 다음 위치
		nx = x + dx[d]
		ny = y + dy[d]

		# 범위 안, 뱀 몸에 안부딪치면
		if 0 <= nx < n and 0 <= ny < n and maps[nx][ny] != 1 : 
			if maps[nx][ny] == 0 : # 빈칸
				x,y = snake.popleft() # 꼬리 자름
				maps[x][y] = 0 # 맵에 표시
				
			maps[nx][ny] = 1 # 사과면
			snake.append([nx,ny]) # 몸 늘림
			if answer == int(directions[cnt][0]) :
				if directions[cnt][1] == "L" :
					d = (d+1)%4
				else : 
					d = (d-1)%4
				cnt+=1
			answer +=1
			x,y = nx,ny
		else : 
			return
		
				


apples = []
directions = []

n = int(input())
k = int(input())
for _ in range(k):
	apples.append(list(map(int, input().split())))
l = int(input())
for _ in range(l):
	directions.append(list(map(str, input().split())))

maps = [[0]*n for _ in range(n)]
answer = 0 
directions.append([0,0])
for apple in apples : 
	x,y = apple
	maps[x-1][y-1] = 2
# 남 동 북 서
dx = [1,0,-1,0]
dy = [0,1,0,-1]
dfs()
print(answer)
		
