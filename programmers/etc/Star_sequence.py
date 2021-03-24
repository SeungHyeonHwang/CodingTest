
"""
스타수열 x 
x는 길이 2이상 짝수
x의 부분집합 n은 서로 교집합 원소 1개이상
하나의 부분집합내 동일원소 x 
"""

from collections import Counter
def solution(a):
	answer = 0

	for com in Counter(a).keys() : 
		i = 1
		ans = 0
		while i < len(a)-1 : 
			if a[i-1] != a[i] and com in [a[i-1],a[i]]:
				ans+=2
				i+=2
			elif a[i-1] != a[i+1] and com in [a[i-1],a[i+1]]:
				ans+=2
				i+=3
			else : 
				i+=1

		answer = max(answer, ans)
	return answer
aa = [[0],[5,2,3,3,5,3],
	[0,3,3,0,7,2,0,2,2,0]]
for a in aa:
	print(solution(a))
	