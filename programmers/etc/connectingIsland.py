
def find_parent(parent, x):
	if parent[x] != x:
		parent[x] = find_parent(parent, parent[x])
	return parent[x]

def union_parent(parent,a,b):
	a = find_parent(parent,a)
	b = find_parent(parent,b)
	if a < b:
		parent[a] = b
	else : 
		parent[b] = a


def solution(n, costs):
	answer = 0
	nodes = set()
	for cost in costs:
		nodes.add(cost[0])
		nodes.add(cost[1])

	parent = [0]*len(nodes)
	for i in range(len(parent)):
		parent[i] = i
	costs.sort(key=lambda x:x[-1])
	for cost in costs:
		if find_parent(parent, cost[0]) != find_parent(parent, cost[1]) : 
			union_parent(parent, cost[0], cost[1])
			answer += cost[-1]
	return answer


n = 6
costs = [[0, 1, 5], [0, 3, 2], [0, 4, 3], [1, 4, 1], [3, 4, 10], [1, 2, 2], [2, 5, 3], [4, 5, 4]]
# 답 11
print(solution(n, costs))