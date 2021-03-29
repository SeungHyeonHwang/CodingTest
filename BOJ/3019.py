

def solution(c,p):
	answer = 0
	
	if p == 1:
		answer+=c
		for i in range(c-3):
			if bt[i] == bt[i+1] and bt[i+1] == bt[i+2] and bt[i+2] == bt[i+3]:
				answer+=1
	elif p == 2:
		for i in range(c-1):
			if bt[i] == bt[i+1] :
				answer+=1
	elif p == 3:
		for i in range(c-2):
			if bt[i] == bt[i+1] and bt[i+1] == bt[i+2]-1:
				answer+=1
		for i in range(c-1):
			if bt[i] == bt[i+1]+1:
				answer+=1
	elif p == 4:
		for i in range(c-2):
			if bt[i]-1 == bt[i+1] and bt[i+1] == bt[i+2] :
				answer+=1
		for i in range(c-1):
			if bt[i]+1 == bt[i+1]:
				answer+=1
	elif p == 5 : 
		for i in range(c-2):
			if bt[i] == bt[i+1] and bt[i+1] == bt[i+2]:
				answer+=1
		for i in range(c-1):
			if bt[i]+1 == bt[i+1]:
				answer+=1
		for i in range(c-2):
			if bt[i] == bt[i+1]+1 and bt[i+1]+1 == bt[i+2]:
				answer+=1
		for i in range(c-1):
			if bt[i] == bt[i+1]+1:
				answer+=1
	elif p == 6 :
		for i in range(c-2):
			if bt[i] == bt[i+1] and bt[i+1] == bt[i+2]:
				answer+=1
		for i in range(c-1):
			if bt[i] == bt[i+1] :
				answer+=1	
		for i in range(c-2):
			if bt[i]+1 == bt[i+1] and bt[i+1] == bt[i+2] :
				answer+=1	
		for i in range(c-1):
			if bt[i] == bt[i+1]+2  :
				answer+=1	
	elif p == 7 : 
		for i in range(c-2):
			if bt[i] == bt[i+1] and bt[i+1] == bt[i+2]:
				answer+=1
		for i in range(c-1):
			if bt[i]+2 == bt[i+1]  :
				answer+=1	
		for i in range(c-2):
			if bt[i] == bt[i+1] and bt[i+1] == bt[i+2]+1 :
				answer+=1	
		for i in range(c-1):
			if bt[i] == bt[i+1] :
				answer+=1	
	return answer

c,p = map(int, input().split())
bt = list(map(int, input().split()))
print(solution(c,p))