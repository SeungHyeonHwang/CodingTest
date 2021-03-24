




def find_parent(parent, x):
	if x != parent : 
		parent[x] = find_parent(parent, parent[x])
	return parent[x]

def union_parent(parent,a,b):
	a = find_parent(parent, a)
	b = find_parent(parent, b)
	if a < b : 
		parenb[b] = a
	else:
		parent[a] = b


import heapq
def solution(n,m):

	q = []
	heapq.heappush(q, [0, 1])
	distance = [int(1e9)]*(n+1)
	distance[1] = 0


	while q :
		dist, now = heapq.heappop(q)
		
		for i in graph[now] : 
			cost = dist + i[1]
			if distance[i[0]] > cost :
				distance[i[0]] = cost
				heapq.heappush(q, [cost, i[0]])

	print(distance)
	return

n = int(input())
m = int(input())
nodes = [list(map(int, input().split())) for _ in range(m)]
graph = [[] for _ in range(n+1)]
for node in nodes :
	graph[node[0]].append([node[1], node[-1]])
	graph[node[1]].append([node[0], node[-1]])
parent = [i for i in range(n+1)]
print(solution(n,m))