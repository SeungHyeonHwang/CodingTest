class Solution(object):
	def climbStairs(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		# n이 1, 1 (1)
		# n이 2, 1,2 (2)
		# n이 3, 1,1,2 (1+2)
		# n이 4, 1111, 112, 121, 211, 22 (3+2)
		# n이 5, 11111, 1112, 1121, 1211, 2111, 122, 212, 221 (5+3)
		# n이 6, 111111, 11112*5, 1122, 1212, 2112, 2121, 2211, 1221, 222 (13)	 

		dp = [1]*n
		dp[1] = 2
		if n == 1: return dp[0]
		if n == 2: return dp[1]
		for i in range(2,n):
			dp[i] = dp[i-1]+dp[i-2]
		return dp[n-1]

n = 3
print(Solution().climbStairs(n))