
"""
야구문제 
시간초과로 인한 답지 참고
b1b2b3 대신 pos 배열로 했더니 시간초과 
"""

def solution(n):
	
	maxScore = 0 
	# 선수 순서
	for order in permutations([i for i in range(1,9)]):
		order = list(order)
		order.insert(3, 0)
		i = 0
		score = 0
		for each_inning in inning : 
			b1,b2,b3 = 0,0,0
			outState = 0
			while outState < 3 : 
				if not each_inning[order[i]] :
					outState+=1
				elif each_inning[order[i]]  == 1:
					score+=b3
					b3,b2,b1 = b2,b1,1 
				elif each_inning[order[i]] == 2:
					score+=(b3+b2)
					b3,b2,b1 = b1,1,0
				elif each_inning[order[i]] == 3:
					score+=(b3+b2+b1)
					b3,b2,b1 = 1,0,0
				elif each_inning[order[i]] == 4 :
					score+=(b3+b2+b1+1)
					b3,b2,b1 = 0,0,0
				i=(i+1)%9
		maxScore = max(maxScore, score)


	return maxScore 

import sys

from itertools import permutations
#input() = sys.stdin.readline

n = int(input())
inning = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

"""
file = open("e6.txt")
for i,f in enumerate(file) : 
	if i == 0 : 
		n = int(f)
		inning = [[0]*n for _ in range(n)]
	else  :
		inning[i-1] = list(map(int, f.split()))
"""
print(solution(n))