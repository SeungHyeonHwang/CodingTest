class Solution:
	def reverse(self, x: int) -> int:
		ans = 0
		s = str(x)
		if x < 0 :
			s = s[1:]
			ans = int('-'+''.join(reversed(s)))
		else :
			ans = int(''.join(reversed(s)))
	
		minNum = -(2**31)
		maxNum =  2**31 - 1
		if ans < minNum or ans > maxNum :
			return 0 
		else : 
			return ans

print(Solution().reverse(123))