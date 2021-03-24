# 상원이의 연속 합

# 연속합이 나오면 1, 아니면 0 
def dfs(result, num):
	if result+num == n : return 1
	elif result+num > n: return 0
	else : return dfs(result+num, num+1) 

def solution(n):

	answer = 0
	idx = 1
	# 1 부터 증가하며 dfs로 탐색
	while idx <= n :
		answer+=dfs(0, idx)
		idx+=1	
	return answer

n = int(input())
print(solution(n))
