class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs : 
            return ''
        if len(strs)==1 : 
            return strs[0] if strs[0].isalpha() else  ''

        strs.sort()
        common = ''
        preStr = list(strs[0])
        pre_l, min_l = len(preStr), len(strs[1])

        for currStr in strs[1:]:
            min_l = min(min_l, len(currStr))
            for i in range(min(pre_l, min_l)):
                if preStr[i] != currStr[i] : 
                    preStr[i] = '0'					
                    min_l-=1
        ans = ''
        for i in range(pre_l):
            if preStr[i].isalpha() :
                ans += preStr[i]
            else : 
                break
        return ans
		
strs =[""]
print(Solution().longestCommonPrefix(strs))