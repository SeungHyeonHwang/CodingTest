
from collections import deque

def solution(N,M,K,A,B,a_list,b_list,t_list) : 

	ans = 0
	result = [0]*K
	clerkA = [[] for _ in range(N)]
	clerkB = [[] for _ in range(M)]
	q1 = deque()
	q2 = deque()
	t = 0
	go = True
	idx = 0 

	while t<25000 : 
		# A고객 대기 
		while idx < K and t == t_list[idx] :
			q1.append(idx+1) # 고객번호
			idx+=1
		# A 창구 순서대로
		for j in range(N):
			# 기존 고객 있으면
			if clerkA[j] :
				clerkA[j][1] += 1
				# 시간 다됐으면 비움
				if a_list[j] == clerkA[j][1]-1 : 
					q2.append(clerkA[j][0])
					clerkA[j] = []
			# 새로운 고객
			if not clerkA[j] and q1 :
				clerkA[j] = [q1.popleft(),1] # 고객 정보
				if j == A-1: 
					result[clerkA[j][0]-1] = 1
	
		# B 창구 순서대로 
		for j in range(M):
			if clerkB[j] :
				clerkB[j][1]+=1
				# 시간 다됐으면 비움
				if b_list[j] == clerkB[j][1]-1 : 
					#if clerkB[j][0] == K-1 :
						#go = False
					clerkB[j] = []
			# 새로운 고객
			if q2 and not clerkB[j] :
				clerkB[j] = [q2.popleft(),1] 
				if j == B-1: 
					result[clerkB[j][0]-1] += 1
		t+=1

	for i,r in enumerate(result) : 
		if r == 2 :
			ans += i+1 

	return -1 if not ans else ans

"""
2 2 6 1 2    # n m k A B   // n 접수창구, m 정비창구
3 2 		 # a
4 2			 # b 
0 0 1 2 3 4  # t
"""

file = open("ex2.txt")
for i,f in enumerate(file):
	if i == 0 : 
		N,M,K,A,B = map(int, f.split())
	if i == 1:
		a_list = list(map(int, f.split()))
	if i == 2:
		b_list = list(map(int, f.split()))
	else:
		t_list = list(map(int, f.split()))

print(solution(N,M,K,A,B,a_list,b_list,t_list))