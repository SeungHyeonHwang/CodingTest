"""
괄호의 값

"""


def solution():
	
	answer = []
	stack = []

	for b in bracket :
		# 올바르지 않은 괄호
		if not stack and b in [')',']'] :
			return 0 

		# 닫는 괄호
		if b in [')',']'] :
			if stack[-1] == '(':
				stack.pop()

				pass
			elif stack[-1] == '[':
				stack.pop()
			
				pass

		# 중복 여는 괄호
		if stack : 
			if stack[-1] == b :
				if b == '(' :
					
				elif b == '[' : 
				

		stack.append(b)
	return answer


#bracket = list(map(str, input()))
bracket = list("(([](([]))))")  # 
#bracket = list("(()[[]])([])")
print(solution())
