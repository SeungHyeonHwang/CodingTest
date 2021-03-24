

def find_parent(parent, x, lst) : 
	if parent[x] != x :
		lst.append(parent[x])
		parent[x] = find_parent(parent, parent[x], lst)
	return parent[x]

def solution(n,s,e,m):

	if s == e :
		return 0 
	
	a = find_parent(parent,s,s_lst)
	b = find_parent(parent,e,e_lst)
	if a != b :
		return -1

	for i,p1 in enumerate(s_lst) :
		for j,p2 in enumerate(e_lst): 
			if p1 == p2 : 
				return i+j



n = int(input())
s,e = map(int, input().split())
m = int(input())
relation = [list(map(int, input().split())) for _ in range(m)]
parent = [i for i in range(n+1)]
s_lst, e_lst = [s], [e]
for r in relation : 
	parent[r[1]] = r[0]

print(solution(n,s,e,m))