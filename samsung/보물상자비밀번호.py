
from collections import defaultdict
#123456789ABCDEF
def solution(n,k,s) : 
	pl = len(s)//4
	
	dictionary = defaultdict(int)
	s = list(s)
	# pl번 회전
	for r in range(pl):
		
		if r > 0 : 
			end = s.pop()
			s.insert(0,end)
		# 총 4변
		for i in range(4):
			# 한변에 pl만큼 있음
			# 한변 담을 숫자
			num = ''
			for j in range(pl): 
				num+=s[pl*i+j]
			# 없으면 저장
			if int(num, 16) not in dictionary.keys() : 
				dictionary[int(num, 16)] = 1
	return sorted(dictionary.keys(), key=lambda x:x, reverse=True)[k-1]



T = int(input())
for _ in range(T):
	n,k = map(int, input().split())
	s = input()
	print(solution(n,k,s))