
# 참조 
# https://velog.io/@rapsby/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%97%AC%ED%96%89%EA%B2%BD%EB%A1%9C-python


def solution(tickets):
	routes = {}
	for t in tickets:
		routes[t[0]] = routes.get(t[0], []) + [t[1]]
	for r in routes:
		routes[r].sort(reverse=True)

	stack = ['ICN']
	path = []
	while stack:
		top = stack[-1]
		if top in routes and routes[top]:
			stack.append(routes[top].pop())
		else:
			path.append(stack.pop())
	return path[::-1]



tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
print(solution(tickets))
