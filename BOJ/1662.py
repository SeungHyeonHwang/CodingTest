


# 33(562(71(9))) 

def solution(s):
	answer = 0
	length = 0
	stack = []
	mul = ''
	result = 1
	for c in s :
		if c.isdigit():
			length+=1
			mul = c
		elif c == '(':
			stack.append([mul, length])
			length = 0
		else : 
			m, num = stack.pop()
			result *= (int(m)*length+num-1)
			print(m,num,result)
	return result

s = list(map(str, input()))
print(solution(s))