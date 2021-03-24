

def solution(m, n, puddles):
	# 2차원 dp 테이블
	dp = [[0]*m for _ in range(n)]
	# 집 학교 붙어있어도 1
	dp[0][0] = 1
	for i in range(n):
		for j in range(m):
			# puddle 이면 다음
			if [j+1,i+1] in puddles : continue
			# 왼쪽있으면
			if j-1>=0 :
				dp[i][j] += dp[i][j-1] 
			# 오른쪽있으면
			if i-1>=0 :
				dp[i][j] += dp[i-1][j]

		
	for i in range(n):
		print(dp[i])
	return dp[n-1][m-1]%(int(1e9)+7)

m = 1
n = 1
puddles =[[2, 2]]
print(solution(m,n,puddles))