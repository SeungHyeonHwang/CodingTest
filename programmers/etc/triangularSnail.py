def solution(n):
	answer = []
	arr = [[0]*(n+1) for _ in range(n+1)]
	offset = [0,0] # 방향, 삽입 offset 
	arr[1][0] = 1
	num = 0
	cnt = 1
	for i in range(n):
		for j in range(n-i): 
			num+=1
			if num == 1 :
				continue
			# 내려갈때
			if offset[0] == 0 :
				arr[j+cnt+offset[1]][offset[1]] = num
			# 옆으로 갈때 
			elif offset[0] == 1:
				arr[n-offset[1]][j+1+offset[1]] = num 

			elif offset[0] == 2:
				arr[n-1-j-offset[1]][n-offset[1]] = num

		# 1번 돌면 방향 변경 
		offset[0]+=1
		# 3번 돌면 삽입 위치 변경 
		if offset[0]%3 == 0  :
			offset[0]%=3
			offset[1]+=1
			cnt+=1

	for i in range(n+1):
		for j in range(n+1):
			if arr[i][j] :
				answer.append(arr[i][j]) 
	return answer

n = 6
print(solution(n)) 