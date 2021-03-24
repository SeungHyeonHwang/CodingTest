"""
처음 완전탐색으로 풀어서 틀림 
"""
def cal(a, b, oper):
	if oper == 0 :
		return a + b
	elif oper == 1 : 
		return a - b
	elif oper == 2 :
		return a * b
	# // 는 내림이기 때문에 int 버림으로 처리.
	else : 
		return int(a/b)

 
def dfs(curr, idx, numbers):
	global maxNum, minNum
	if idx >= len(numbers):
		maxNum = max(curr, maxNum)
		minNum = min(curr, minNum)
		return
	# 4종류 oper를 다시 각각 재귀
	for i in range(4):
		if operands[i] :	
			# 재귀 전 oper 빼줌
			operands[i]-=1 
			dfs(cal(curr, numbers[idx], i), idx+1, numbers)
			# 현상태에서 다른 oper 재귀를 위해 다시 +1
			operands[i]+=1

import itertools
def solution(n, operands, numbers):
	dfs(numbers[0], 1, numbers)
	return maxNum-minNum

minNum = int(1e9)
maxNum = -int(1e9)
files = open("ex1.txt")
for i,f in enumerate(files):
	if i== 0 : 
		n = int(f)
	if i == 1 :
		operands = list(map(int, f.split()))
	else : 
		numbers = list(map(int, f.split()))
print(solution(n, operands, numbers))

"""
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
 	n = int(input())
    operands = list(map(int, input().split()))
    numbers = list(map(int, input().split()))  
    print("#%d %d"%(test_case, solution(n,operands, numbers)))
"""