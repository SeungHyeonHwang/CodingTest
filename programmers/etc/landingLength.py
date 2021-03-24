


def solution(dirs):
	answer = 0
	maps = [[0]*11 for _ in range(11)]

	visited = set()
	directions = {"U":0,"R":1,"D":2,"L":3}

	dx = [-1,0,1,0]
	dy = [0,1,0,-1]

	x,y = 5,5

	for d in dirs : 
		r = directions[d]
		nx = x+dx[r]
		ny = y+dy[r]
		if 0<=nx<=10 and 0<=ny<=10:


			if ((x,y),(nx,ny)) not in visited :
				visited.add( ((x,y),(nx,ny)) )
				visited.add( ((nx,ny),(x,y)) )
				answer+=1
			x = nx
			y = ny

	return answer


ss = [	
		"ULURRDLLU",
		"LULLLLLLU",
		"UUDD"
	]

for s in ss : 
	print(solution(s))	
	print()