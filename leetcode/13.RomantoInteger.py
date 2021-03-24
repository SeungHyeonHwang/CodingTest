class Solution(object):
	def romanToInt(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		romantoInt = {'I':1,'IV':4,'V':5,'IX':9,\
						'X':10,'XL':40,'L':50,'XC':90,\
						'C':100,'CD':400,'D':500,'CM':900,'M':1000}
		integer = 0
		i=0
		while True :
			start,end = 0,2
			if s[start+i:end+i] not in romantoInt.keys():
				end-=1
			integer+=romantoInt[s[start+i:end+i]]
			i+=end
			if i > len(s)-1:
				return integer
s = "MCMXCIV"
print(Solution().romanToInt(s))