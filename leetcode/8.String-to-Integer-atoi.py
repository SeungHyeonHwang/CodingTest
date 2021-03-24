class Solution:
	def myAtoi(self, s: str) -> int:

		
		digit = s.strip()
		if not digit : return 0 
		sign = -1 if digit[0] == '-' else 1
		if digit[0] in ['-','+'] : digit = digit[1:]
	
		l = '0'
		i = 0
		while i < len(digit) and digit[i].isdigit() : 
			l += digit[i]
			i+=1

		ans = sign*int(l)
		return max(-(2**31), min(2**31-1, ans))


s = " "
print(Solution().myAtoi(s))
        