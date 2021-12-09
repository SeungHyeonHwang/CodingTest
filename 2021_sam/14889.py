
import itertools 

n = int(input())
tims = [list(map(int,input().split())) for _ in range(n)]

min_num = int(1e9)
for start_tim_mem in itertools.combinations([i for i in range(len(tims))], len(tims)//2) : 
	start_tim = 0
	link_tim = 0

	for start in itertools.combinations(start_tim_mem, 2) : 
		start_tim+=tims[start[0]][start[1]]
		start_tim+=tims[start[1]][start[0]]
	
	link_tim_mem = list(set([i for i in range(len(tims))]) - set(start_tim_mem))

	for link in itertools.combinations(link_tim_mem, 2) :
		link_tim+=tims[link[0]][link[1]]	
		link_tim+=tims[link[1]][link[0]]

	if abs(start_tim - link_tim) < min_num :
		min_num = abs(start_tim - link_tim) 
print(min_num)