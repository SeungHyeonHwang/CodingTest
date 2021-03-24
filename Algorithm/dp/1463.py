# 1로 만들기
def solution(n):
	inf = int(1e6)+1
	dp = [inf]*(n+2)
	dp[1] = 0
	dp[2] = 1
	for i in range(3,n+1):
		if i%2 == 0 :
			dp[i] = dp[i//2]+1
		if i%3 == 0 :
			dp[i] = min(dp[i], dp[i//3]+1)
		dp[i] = min(dp[i], dp[i-1]+1)
	return dp[n]

n = int(input())
print(solution(n))