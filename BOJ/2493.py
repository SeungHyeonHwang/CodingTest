
"""
탑
n은 1이상 500,000 이하로 완전탐색으로 해결할 수 없음.
처음 local max idx를 찾아 local~i까지 구했지만,
풀이를 참조
stack을 이용하여 stack에 필요한 높이만 저장하여 효율적으로 비교 
"""


def solution(n):
	answer = [0]
	stack = [[0, tops[0]]]
	for i in range(1, n):
		
		while stack : 
			if stack[-1][1] > tops[i] :
				answer.append(stack[-1][0]+1)
				break
			else : 
				stack.pop()
		if not stack : 
			answer.append(0)
		stack.append([i, tops[i]])
			
	return " ".join(map(str, answer))


n = int(input())
tops = list(map(int, input().split()))
print(solution(n))