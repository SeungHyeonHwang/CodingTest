
class Solution:
	def convert(self, s: str, numRows: int) -> str:
        
		d = ['']*numRows
		down = 1
		j = 0
		while j < len(s) : 

			for i in range(numRows) : 
				if j >= len(s):
					break
				if down :
					d[i] +=s[j]
					j+=1
				if not down and 0<i<numRows-1 : 
					d[numRows-i-1] += s[j]
					j+=1
				if i == numRows-1 :
					down = (down+1)%2
		
		ans =''
		for i in range(numRows):
			ans += d[i]
		return ans

s = "A"
numRows = 1
print(Solution().convert(s, numRows))
