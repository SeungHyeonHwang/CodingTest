def solution(tickets):

	answer = []
	routes = {}

	for route in tickets:
		if route[0] in routes.keys():
			routes[route[0]].append(route[1])
		else : 
			routes.setdefault(route[0], [route[1]])

	for ticket in routes.keys():
		routes[ticket] = sorted(routes[ticket])
	

	key = "ICN"
	answer.append(key)
	while key in routes.keys() : 

		answer.append(routes[key][0])
		key = routes[key].pop(0)

		if key in routes.keys() and not routes[key] :
			routes.pop(key)
		
	return answer