# 숫자게임
# 참조 

def solution(A, B):
	answer = 0

	A.sort(reverse=True)
	B.sort()

	while B :
		if A[-1] < B[0]:
			A.pop(-1)
			answer+=1
		B.pop(0)
	return answer

A = [2,2,2,2]
B = [1,1,1,1]

print(solution(A,B))



