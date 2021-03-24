
# 동철이의 프로그래밍 대회



file = open("ex3.txt")
for i,f in enumerate(file):
	if i == 0:
		n,m = map(int, f.split())
		a = [[0]*m for _ in range(n)]
	else : 
		a[i-1] = list(map(int, f.split()))

maxScore = 0
for i in range(n):
	score = a[i].count(1) # 1 카운트
	a[i].append(score)
	maxScore = max(score, maxScore)
winner = 0
for i in range(n):
	if a[i][-1] == maxScore :
		winner +=1 # 최고점이면 사람 수 구함
print(winner, maxScore)