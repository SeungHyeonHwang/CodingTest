

import copy

answer = 0
def dfs(ecopy, i, n, result):
	global answer
	ecopy.pop(i)
	if len(ecopy) <= 2:
		answer = max(answer, result)
		return
	for i in range(1,len(ecopy)-1):
		dfs(copy.deepcopy(ecopy), i, n, result+ecopy[i-1]*ecopy[i+1])

def solution(n):
	global answer
	for i in range(1,n-1):
		dfs(copy.deepcopy(energy), i, n, energy[i-1]*energy[i+1])
	return answer

n = int(input())
energy = list(map(int, input().split()))
print(solution(n))