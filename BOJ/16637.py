"""
괄호 추가하기
처음에 answer = 0 으로 초기화하여 틀렸음.
최댓값이라 하여도 음수가 나올 수 있는 경우 인지하기

"""

def bracket(eq, i, l):
	result = 0
	if i >= l :
		after_bracket.append(eq) 
		return

	# 현재 위치 괄호 
	if eq[i] == "+":
		result = (int(eq[i-1])+int(eq[i+1]))
	elif eq[i] == "-":
		result = (int(eq[i-1])-int(eq[i+1]))
	elif eq[i] == "*":
		result = (int(eq[i-1])*int(eq[i+1]))

	next_eq = eq[:i-1]+[result]+eq[i+2:]
	
	bracket(next_eq, i+2, len(next_eq))
	bracket(eq, i+2, len(eq))

def dfs(eq, l, result):

	if l < 3:
		return result

	if eq[1] == "+":
		result+=int(eq[2])
	elif eq[1] == "-":
		result-=int(eq[2])
	elif eq[1] == "*":
		result*=int(eq[2])
	return dfs([result]+eq[3:], l-2,result)


def solution(n):
	answer = -(2**31)
	bracket(equation, 1, n)
	for eq in after_bracket:
		answer = max(answer, dfs(eq, len(eq), int(eq[0])))

	return max(min(answer, 2**31), -(2**31))

n = int(input())
equation = list(map(str, input()))
after_bracket = []
print(solution(n))

           