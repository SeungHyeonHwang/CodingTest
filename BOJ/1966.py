"""
프린터 큐

"""

from collections import deque

def solution(n,m) : 
	q = deque()
	order = []
	for i,p in enumerate(prior):
		q.append([p,i])
		order.append(p)
	order.sort()

	i = 1
	while q :
		p = q.popleft() 
		if p[0] == order[-1]:
			order.pop()		
			if p[1] == m :
				return i
			i+=1
		q.append(p)



test_case = int(input())
for t in range(test_case):
	n,m = map(int, input().split())
	prior = list(map(int, input().split()))
	print(solution(n,m))