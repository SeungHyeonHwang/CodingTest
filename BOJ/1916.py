

import heapq

def solution(n,m):
	q = []
	route = [[] for _ in range(n+1)]
	for b in bus : 
		route[b[0]].append((b[2],b[1]))
	
	inf = int(1e9)
	distance = [inf]*(n+1)

	heapq.heappush(q, (0, target[0]))
	distance[target[0]] = 0
	while q :
		dist, now = heapq.heappop(q)
		if distance[now] < dist : 
			continue
		for d in route[now]:
			cost = d[0] + dist
			if distance[d[1]] > cost :
				heapq.heappush(q, (cost, d[1]))
				distance[d[1]] = cost
	return distance[target[1]]


n = int(input())
m = int(input())
bus = [list(map(int, input().split())) for _ in range(m)]
target = list(map(int, input().split()))
print(solution(n,m))