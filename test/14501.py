
n=int(input())
TP = [[] for _ in range(n)]
for i in range(n):
	TP[i] = list(map(int, input().split()))
	TP[i].append(i)
stack = []
curr_day=len(TP)
for i in range(len(TP)-1,-1,-1):
	tp = TP[i]
	curr_day-=1
	# 여유가 있으면 바로 저장 
	if tp[0] <= curr_day :
		stack.append((tp[-1],tp[0],tp[1]))
		print(curr_day, tp[0], stack)
		curr_day-=tp[0]
		
	# 스택이 있으면
	elif len(TP)-tp[0]+1 >= tp[1] and stack : 
		temp_day=curr_day
		salary,cnt = 0,0
		for j in range(len(stack)-1,-1,-1):
			cnt+=1
			temp_day+=stack[j][1]
			salary+=stack[j][-1]
			if temp_day >= tp[-1]:
				break
		if salary < tp[1] :
			for _ in range(cnt):
				day,spend,sal = stack.pop()
				curr_day+=spend
			stack.append((tp[-1],tp[0],tp[1]))
			curr_day-=tp[0]
answer=0
for st in stack:
	answer+=st[-1]
print(answer)
