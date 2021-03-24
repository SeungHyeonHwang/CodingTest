"""
arr : memo
num : N을 i번 사용한 경우 저장
4중 for : 위 경우와 중복되지 않는 연산자에 의한 사용 경우의 수
수행 후 위 num(arr[i]) 에 set 형태로 저장
arr[i] 에 답 있는지 체크
"""

def solution(N, number):
	answer = 0
	dp = [set() for _ in range(8)]
	for i,num in enumerate(dp,start=1):
		num.add(int(str(N)*i))
	
	for i in range(1,len(dp)):
		for j in range(i):
			for x in dp[j]:
				for y in dp[i-j-1]:
					print(i,j,x,y)
					
					dp[i].add(x+y)
					dp[i].add(x-y)
					dp[i].add(x*y)
					if y!=0:
						dp[i].add(x//y)
					print(dp)
					print()
		if number in dp[i]:
			answer = i+1
			break
	# break 한번도 안되었으면 
	else :
		answer = -1

	return answer



print(solution(5,12))