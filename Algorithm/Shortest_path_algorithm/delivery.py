
def dijksta():

	while q :
		dist, now = heapq.heappop(q)

		if distance[now] < dist :
			continue

		# 인접 노드
		for i in graph[now]:
			cost = dist + i[1]
			if cost < distane[i[1]] :
				cost = distane[i[1]] 
				heapq.heappush(q,(cost,i[1]))

def solution(n, road, k):
	
	import heapq
	answer = 0
	INF = int(10e9)
	graph = [[] for _ in range(n+1)]
	distance = [INF]*(n+1)

	# 그래프 초기화
	for i in road : 
		graph[i[0]].append((i[1],i[2]))
		graph[i[1]].append((i[0],i[2]))
	start = 1
	distance[start] = 0
	q = []
	heapq.heappush(q,(0, start))
	while q :
		dist, now = heapq.heappop(q)
		
		if distance[now] < dist :
			continue

		# 인접 노드
		for i in graph[now]:
			cost = dist + i[1]
			if cost < distance[i[0]] :
				distance[i[0]]  = cost
				heapq.heappush(q,(cost, i[0]))

	for dis in distance : 
		if dis <= k :
			answer+=1
	return answer

n = 6
road = [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]]	
k = 4
print(solution(n,road,k))