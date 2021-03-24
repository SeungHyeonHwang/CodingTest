
# https://deok2kim.tistory.com/48 참조 
from collections import deque

def solution(n, path, order):

	graph = {n: [] for n in range(n)}

	for s,e in path :
		graph[s].append(e)
		graph[e].append(s)

	pre_order = {}
	aft_order = {}
	for a,b in order : 
	
		if b == 0 :
			return False 
		if a != 0 :	
			pre_order[a] = b
			aft_order[b] = a
	visited = [0]* n
	
	q = deque()
	q.append(0)	
	visited[0] = 1
	while q :
		x = q.popleft()

		for node in graph[x] : 
	
			if node == pre_order.get(aft_order.get(node)) : 
				visited[node] = 2
			
			elif not visited[node] : 
				q.append(node)
				visited[node] = 1
				
				if pre_order.get(node) : 
					if visited[pre_order.get(node)] == 2 : 
						q.append(pre_order.get(node))
						visited[pre_order.get(node)] = 1
					pre_order[node] = 0
	for i in visited : 
		if i == 0 :
			return False
	return True 				



n = 9
path =[[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]]
order = [[8,5],[6,7],[4,1]]
print(solution(n, path, order))
n =9
path =	[[8,1],[0,1],[1,2],[0,7],[4,7],[0,3],[7,5],[3,6]]
order =	[[4,1],[5,2]]	
print(solution(n, path, order))
n = 9
path =	[[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]]	
order = [[4,1],[8,7],[6,5]]
print(solution(n, path, order))