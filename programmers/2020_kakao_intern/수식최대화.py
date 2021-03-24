

from itertools import permutations
import copy

def calculate(form, a,b) : 
	if form == "+" :
		return a+b
	elif form == "-" :
		return a-b
	elif form == '*' :
		return a*b

def solution(expression):
	answer = 0
	operator = []
	form = []
	idx = 0
	for i, ex in enumerate(expression) :
		if not ex.isdigit() : 
			operator.append(ex)
			form.append(expression[idx:i])
			form.append(ex)
			idx = i+1
	form.append(expression[idx:])

	for next_oper in list(permutations(set(operator), len(set(operator)))) :
		formula = copy.deepcopy(form)
		print('연산자 순서', next_oper)

		pos = 0
		while True : 

			for i, oper in enumerate(formula) : 
				if i >= len(formula)-1 :
					pos +=1
					break
				if next_oper[pos] == oper : 
					print('계산전 연산자:', oper, '식: ',formula)
					temp = calculate(oper, int(formula[i-1]), int(formula[i+1]))
					formula.insert(i-1, temp)
					for _ in range(3):
						formula.pop(i)
					print('계산후 연산자:', oper, '식: ',formula)
					print()
					break
			if pos >= len(next_oper) : 
				break
			
				
		print('결과식 : ',formula)
		
		if len(formula) > 1 :
			temp = calculate(formula[1], int(formula[0]), int(formula[2]))
			formula.insert(0, temp)
			for _ in range(3):
				formula.pop(1)
		print('결과 : ',abs(formula[0]))
		print()
		answer = max(answer, abs(formula[0]))
	return answer



# -100*300-450
expression = "100-200*300-500+20"
#expression = "50*6-3*2"
print(solution(expression))

