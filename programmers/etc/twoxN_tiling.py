# 시간초과
def solution(n):
	answer = 0
	"""
	n = 1 : 1
	n = 2 : 2
	n = 3 : 3
	n = 4 : 5
	n = 5 : 8
	"""

	dp = [0]*60000
	dp[0] = 1
	dp[1] = 2
	for i in range(2,n):
		dp[i] = dp[i-1] + dp[i-2]
	return dp[n-1]%(int(1e9)+7)

# 같은 방식 dp 테이블 없이
def solution(n):
	c,a,b = 0,1,2
	for i in range(2,n):
		c = a+b
		a,b = b,c
	return c%(int(1e9)+7)
n= 59999
print(solution2(n))

