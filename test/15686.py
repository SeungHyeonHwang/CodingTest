



from itertools import combinations 

def solution(n,m):
	answer = int(1e9)
	for comb in combinations(chicken, m):
		distance = [int(1e9)]*len(house)
		for x,y in comb:
			for i,(hx,hy) in enumerate(house) : 
				dist = abs(x-hx)+abs(y-hy)
				if distance[i] > dist : 
					distance[i] = dist
		answer = min(sum(distance),answer)

	return answer 

n,m = map(int,input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
house, chicken = [], []
for i in range(n):
	for j in range(n):
		if maps[i][j] == 1:
			house.append((i,j))
		if maps[i][j] == 2 :
			chicken.append((i,j))
print(solution(n,m))