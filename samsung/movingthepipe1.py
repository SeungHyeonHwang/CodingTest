

def movingPipe(x):

	global ans

	if x[0]==n-1 and x[1]==n-1 : 
		ans+=1
		return 

	if x[2] == 0:
		if 0<=x[1]+1 <n:
			if not maps[x[0]][x[1]+1] : 
				movingPipe([x[0],x[1]+1,0])
		if  0<=x[0]+1<n and 0<=x[1]+1<n:	
			if not maps[x[0]][x[1]+1] and not maps[x[0]+1][x[1]+1] and not maps[x[0]+1][x[1]] : 
				movingPipe([x[0]+1,x[1]+1,2])
	elif x[2] == 1:
		if 0<=x[0]+1 <n:
			if not maps[x[0]+1][x[1]] : 
				movingPipe([x[0]+1,x[1],1])
		if  0<=x[0]+1<n and 0<=x[1]+1 <n:		
			if not maps[x[0]][x[1]+1] and not maps[x[0]+1][x[1]+1] and not maps[x[0]+1][x[1]] : 
				movingPipe([x[0]+1,x[1]+1,2])

	elif x[2] == 2:
		if 0<=x[1]+1<n:
			if not maps[x[0]][x[1]+1] : 
				movingPipe([x[0],x[1]+1,0])
		if 0<=x[0]+1 <n:	
			if not maps[x[0]+1][x[1]] : 
				movingPipe([x[0]+1,x[1],1])
		if 0<=x[0]+1<n and 0<=x[1]+1 <n:		
			if not maps[x[0]][x[1]+1] and not maps[x[0]+1][x[1]+1] and not maps[x[0]+1][x[1]] : 
				movingPipe([x[0]+1,x[1]+1,2])


def solution(n):
	
	
	start = [0,1,0]
	movingPipe(start)
	return ans

ans = 0
n = int(input())
maps = [list(map(int,input().split())) for _ in range(n)]
print(solution(n))
"""
file =open("ex3.txt")
for i,f in enumerate(file) : 
	if i == 0 : 
		n = int(f)
		maps = [[0]*n for _ in range(n)]
	else  :
		maps[i-1] = list(map(int, f.split()))

print(solution(n))
"""