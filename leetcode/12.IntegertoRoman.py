class Solution(object):
	def intToRoman(self, num):
		"""
		:type num: int
		:rtype: str

		Symbol       Value
		I             1
		V             5
		X             10
		L             50
		C             100
		D             500
		M             1000
		"""
		romanValue = [1,5,10,50,100,500,1000]
		roman = {1:'I', 5:'V', 10:'X', 50:'L', 100:'C', 500:'D', 1000:'M'}
		ans = ''
		idx = 6
		while idx > 0 : 
			if num%romanValue[idx] != num :
				ans += roman[romanValue[idx]]
				num -= romanValue[idx]
				continue
			idx-=1
		for i in range(num):
			ans += roman[1]
		return ans.replace("DCCCC","CM").replace("CCCC","CD").replace("LXXXX","XC").replace("XXXX","XL").replace("VIIII","IX").replace("IIII","IV")
num = 1
print(Solution().intToRoman(num))