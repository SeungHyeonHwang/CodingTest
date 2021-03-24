"""
후보 추천하기
구현

제출 형식을 list로 하여 계속 틀린 것.
출력 형식을 말해줬으면 좋았을 문제.

"""
def isExisted(y, arr):
	for i,x in enumerate(arr) : 
		if x[-1] == y:
			return [True,i]
	return [False,0]

def solution(n,v):
	answer = []
	t = 0
	stack = []
	for cand in candidates : 
		[isexisted,idx] = isExisted(cand, stack)
		if isexisted :
			stack[idx][1]+=1
		else : 
			if len(stack) >= n : 
				stack.sort(key=lambda x : (-x[1],-x[0]))
				stack.pop()
			stack.append([t,1,cand])
			t+=1

	for p in stack:
		answer.append(p[-1])
	return ' '.join(map(str, sorted(answer)))

n = int(input())
v = int(input())
candidates = list(map(int, input().split()))
print(solution(n,v))