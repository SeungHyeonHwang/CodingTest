class Solution:
	# O(N) (linear time) : 내 풀이
	def isPalindrome(self, x: int) -> bool:
		if x < 0 : return False
		s = str(x)
		for i,a in enumerate(s): 
			if a != s[len(s)-1-i] :
				return False
		return True
	# O(1) (constant time) : 다른사람 알고리즘
	def isPalindromeV(self, x):
		if x < 0:
			return False
		p, res = x, 0
		while p:
			res = res * 10 + p % 10
			p //= 10
		return res == x
x = 12321
print(Solution().isPalindromeV(x))

