# 나의 풀이

# O(N) 풀이 
class Solution:

	def lengthOfLongestSubstring(self, s: str) -> int:

		import copy
		from collections import defaultdict
		ans = []
		string = copy.deepcopy(s)
		
		if s == '':
			return 0 
		while True : 
			i = 0
			dictionary = defaultdict(str)
			
			for a in string :
				if a not in dictionary.keys() :
					dictionary[a] = i
					i+=1
				else : 
					break
			ans.append(len(dictionary.keys()))
			string = string[dictionary[a]+1:]
			
			if not string :
				return sorted(ans, reverse=True)[0]

    # @return an integer
	def lengthOfLongestSubstring_v(self, s):
		start = maxLength = 0
		usedChar = {}
		for i in range(len(s)):
			if s[i] in usedChar and start <= usedChar[s[i]]:
				start = usedChar[s[i]] + 1
			else:
				maxLength = max(maxLength, i - start + 1)
			usedChar[s[i]] = i
		return maxLength

s = "dvdfd1234567zxc aW32323"
print(Solution().lengthOfLongestSubstring(s))
print(Solution().lengthOfLongestSubstring_v(s))