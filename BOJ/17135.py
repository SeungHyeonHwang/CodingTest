"""
캐슬디펜스
"""
from itertools import combinations
import copy
def solution(n,m,d,e):
	answer = 0
	for achers in combinations([i for i in range(m)],3):
		board = copy.deepcopy(maps)
		
		result = 0 
		gameOver = False
		num = e

		while not gameOver and num > 0: 
			enermy = [[] for _ in range(m)]
			for i in range(n-1,-1,-1):
				for j in range(m):
					for acher in achers : 
						if board[i][j] and abs(acher-j)+n-i <= d:
							enermy[acher].append([i,j,abs(acher-j)+n-i])
			

			for i in range(m) :
				if enermy[i] : 
					ne = sorted(enermy[i], key = lambda x : (x[-1], x[1]))[0]
					if board[ne[0]][ne[1]] :
						board[ne[0]][ne[1]] = 0
						result+=1
						num-=1

			for i in range(m):
				if board[n-1][i] :
					num-=1
			board.pop()
			board.insert(0,[0 for _ in range(m)])
		answer = max(answer, result)
	return answer

n,m,d = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
e = len([[i,j] for i in range(n) for j in range(m) if maps[i][j]])

print(solution(n,m,d,e))