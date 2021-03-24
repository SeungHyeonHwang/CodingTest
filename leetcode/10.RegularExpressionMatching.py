class Solution:
	def isMatch(self, s: str, p: str) -> bool:
		dp = [[False]*(len(p)+1) for i in range(len(s)+1)]
		# Update the corner case of matching two empty strings. egg s='a' p='a', so s[0] = p[0]  ==> dp[1][1] == dp[0][0], we can see dp[0][0] need to set True
		dp[0][0] = True
		# Update the corner case of when s is an empty string but p is not.
		# Since each '*' can eliminate the charter before it, the dp table is vertically updated by the one before previous
		for j in range(2,len(p)+1):
			if p[j-1] == '*':  
				dp[0][j] = dp[0][j-2]
		
		for i in range(1,len(s)+1):
			for j in range(1,len(p)+1):
				print(p[j-1], [s[i-1],'.'], dp[i-1][j-1])
				dp[i][j] = (p[j-1] in [s[i-1],'.'] and dp[i-1][j-1]) or (p[j-1] == '*' and ((p[j-2] in [s[i-1],'.'] and dp[i-1][j]) or (dp[i][j-2]))) 
		return dp[len(s)][len(p)]

s =  "aaa"
p = "ab*a"
print(Solution().isMatch(s,p))