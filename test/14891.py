

def rotation(num, dirs, dir_state):
	r,l = gears[num][2],gears[num][-2]
	if dirs == 1 :
		gears[num].insert(0, gears[num].pop())
	else : 
		gears[num].append(gears[num].pop(0))
	if not dir_state :	
		if num+1<4 and r != gears[num+1][-2] : rotation(num+1, -dirs, 1)
		if num-1>=0 and l != gears[num-1][2] : rotation(num-1, -dirs, -1)
	elif dir_state == 1 :
		if num+1<4 and r != gears[num+1][-2] : rotation(num+1, -dirs, 1)
	elif dir_state == -1 :
		if num-1>=0 and l != gears[num-1][2] : rotation(num-1, -dirs, -1)
	
def solution(k):
	answer= 0
	for com in command : 
		rotation(com[0]-1,com[1],0)
	for i in range(4):
		if gears[i][0]:
			answer+=(2**i)
	return answer 


gears = [list(map(int, input())) for _ in range(4)]
k = int(input())
command = [list(map(int,input().split())) for _ in range(k)]
print(solution(k))