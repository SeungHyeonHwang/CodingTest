# 512MB 이내, 124500KB = 124.5MB
# 1초이내, 216 ms

# 회전
def rotation(x,d,k):
	mul=x
	while x <= n :
		for i in range(k):
			if d == 0 : 
				disc[x].insert(0,disc[x].pop(-1))
			else : 
				disc[x].append(disc[x].pop(0))
		x+=mul
# 삭제
def delSame(n,m):
	isDel = False
	delLst = []
	for i in range(1,n+1):
		for j in range(m):
			if disc[i][j] == 'x':
				 continue
			x = disc[i][j]
			
			for k in range(4):
				ni = i + dx[k]
				nj = j + dy[k]
				if 0<ni<n+1 and -1<=nj<m+1:
					if nj == m :
						nj = 0
					if x == disc[ni][nj] : 
						delLst.append((i,j))
						delLst.append((ni,nj))
						isDel = True
	for lst in delLst:
		if disc[lst[0]][lst[1]] != 'x':
			disc[lst[0]][lst[1]] ='x'
	return isDel
# 평균/가감
def cal(n,m):
	summ,cnt = 0,0
	for i in range(1,n+1):
		for j in range(m):
			if disc[i][j] != 'x':
				summ+=disc[i][j] 
				cnt+=1
	avg = summ/cnt if cnt else 0
	for i in range(1,n+1):
		for j in range(m):
			if disc[i][j] == 'x':
				continue
			if disc[i][j] > avg :
				disc[i][j]-=1
	
			elif disc[i][j] < avg:
				disc[i][j]+=1
# 메인
def solution(n,m,t):
	answer = 0
	for i in range(t):
		x,d,k = xdk[i][0], xdk[i][1], xdk[i][2]
		rotation(x,d,k)
		if not delSame(n,m):
			cal(n,m)

	for i in range(1,n+1):
		for j in range(m):
			if disc[i][j] != 'x':
				answer+=disc[i][j]
	return answer 

dx = [-1,0,1,0]
dy = [0,1,0,-1]
"""
file = open('ex3.txt')
for i,f in enumerate(file):
	if i == 0 :
		n,m,t = map(int, f.split())
		disc = [[] for _ in range(n+1)]

		xdk = []
	elif 0<i<=n:
		disc[i] = list(map(int, f.split()))
	else : 
		xdk.append(list(map(int, f.split())))
"""

n,m,t = map(int, input().split())
disc = [[] for _ in range(n+1)]
for i in range(1,n+1):
	disc[i] = list(map(int, input().split()))
xdk = [list(map(int, input().split())) for _ in range(t)]
print(solution(n,m,t))