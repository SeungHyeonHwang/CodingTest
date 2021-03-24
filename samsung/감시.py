
# 참고 : https://pacific-ocean.tistory.com/370

import copy
import sys
input = sys.stdin.readline 

# 방향 별로 map에 맵핑
def scan(arr, x,y,d):
	for i in d :
		nx, ny = x,y
		while True : 
			nx+=dx[i]
			ny+=dy[i]
			if 0 <=nx<n and 0<=ny<m:
				if arr[nx][ny] == 6:
					break
				elif arr[nx][ny] == 0 :
					arr[nx][ny] = "#"
			else : 
				break

def dfs(arr, num) : 
	global answer
	
	temp = copy.deepcopy(arr)
	if num == len(cctv_list) : 
		cnt = 0
		for i in range(n) : 
			cnt+=temp[i].count(0)
		answer = min(answer, cnt)
		return
	x,y,cctv = cctv_list[num]

	# 경우의 수 
	for d in direction[cctv] : 
		# 현재 temp 에 방향별로 맵핑
		scan(temp, x,y,d)
		# 현재 temp(num) 를 dfs를 통해 temp(num+1)에 맵핑
		dfs(temp, num+1)
		# 경우의 수마다 num 상태에 대한 temp에 맵핑
		temp = copy.deepcopy(arr)



if __name__ == "__main__" : 

	n,m = map(int, input().split())
	maps = [list(map(int, input().split())) for _ in range(n)]

	cctv_list = []
	for i in range(n) : 
		for j in range(m) : 
			if 0 < maps[i][j] < 6 :
				cctv_list.append([i,j, maps[i][j]])

	#    남 서 북 동
	dx = [-1,0,1,0]
	dy = [0,-1,0,1]

	direction = [[],
				[[0],[1],[2],[3]],
				[[0,2],[1,3]],
				[[2,3],[3,0],[0,1],[1,2]],
				[[1,2,3],[2,3,0],[0,1,3],[0,1,2]],
				[[0,1,2,3]]
				]

	answer = int(1e9)
	dfs(maps,0)
	print(answer)

