"""
https://www.acmicpc.net/problem/2637
"""

from collections import deque
def solution(n,m):

	q = deque()
	# 부품 정보 
	parts = [[0]*(n+1) for _ in range(n+1)]
	for i in range(1,n+1):
		# 진입 차수 없으면 큐에 넣기
		if indegree[i] == 0 :
			# 진입 차수 없는 부품 초기 개수 초기화
			parts[i][i] = 1
			q.append(i)
	# 큐 빌때까지
	while q: 
		# i : 현재 부품
		i = q.popleft()
		# ni : 다음 부품, need : 개수
		for ni, need in graph[i]:
			# 진입 차수 줄이고
			indegree[ni]-=1
			# 다음 부품 parts[ni] = 현재 parts[i]의 부품 * need(개수) 
			for j in range(1,n+1):
				parts[ni][j] += (parts[i][j]*need)
			# 진입 차수 0 이면 큐에 넣을 수 있음
			if indegree[ni] == 0 :
				q.append(ni)
	# 모든 큐가 돌아가면 부품 테이블을 만들었으므로
	for i in range(1,n+1):
		# 원하는 부품 n 에 필요한 정보 출력
		if parts[n][i] :
			print("%d %d"%(i, parts[n][i]))
	return

n = int(input())
m = int(input())
connect = [list(map(int,input().split())) for _ in range(m)]
# 그래프
graph = [[] for _ in range(n+1)]
# 진입 차수
indegree = [0]*(n+1)
for c in connect : 
	graph[c[1]].append((c[0], c[2]))
	indegree[c[0]]+=1
solution(n,m)
