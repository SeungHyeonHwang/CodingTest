"""
게리멘더링
"""
from itertools import combinations
from collections import deque

def connection(visited, comb, l, cnt):
	
	visited[comb[0]] = 1
	if cnt == l : 
		return True
	q = deque()
	q.append(comb[0])
	while q :
		p = q.popleft()
		for i,v in enumerate(maps[p]):
			if v and not visited[i] and i in comb:
				visited[i] = 1
				q.append(i)
				cnt+=1
	if cnt >= l : 
		return True
	return False

def solution(n):
	answer = int(1e9)
	
	lst = [i for i in range(1,n+1)]
	# 1 구획 개수
	for i in range(1, n):
		# 1 구획 조합
		for comb1 in combinations(lst, i):
			# 연결 그래프 확인 
			visited1 = [0]*(n+1)
			# 1 조합내 연결성 확인
			if connection(visited1, comb1, len(comb1), 1):
				comb2 = list(set(lst)-set(comb1))
				visited2 = [0]*(n+1)
				# 2 조합내 연결성 확인
				if connection(visited2, comb2, len(comb2), 1):
					val1, val2 = 0,0
					for c1 in comb1 :
						val1+=population[c1-1]
					for c2 in comb2:
						val2+=population[c2-1]
					answer = min(answer, abs(val1-val2))	
	return answer if answer < int(1e9) else -1

n = int(input())
population = list(map(int, input().split()))
maps = [[0]*(n+1) for _ in range(n+1)]
for i in range(1,n+1):
	info = list(map(int, input().split()))
	for j in range(1,info[0]+1):
		maps[i][info[j]] = 1
		maps[info[j]][i] = 1

print(solution(n))