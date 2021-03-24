
"""
1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다. 
2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다. 단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있습니다. 

3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다. 
  3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다. 

4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다. 
  4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다. 
  4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다. 
  4-3. ')'를 다시 붙입니다. 
  4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다. 
  4-5. 생성된 문자열을 반환합니다.
"""



# 3. 올바른지 검사
def isCorrect(u) : 
	d = {'(':0, ')':0}
	for i,s in enumerate(u) :
		d[s] += 1
		if d[')'] > d['('] : 
			return False
	return True

# 2. u와 v를 나눔
def uv(p,ans) : 
	if p == '' : 
		return ''
	d = {'(':0, ')':0}
	for i,s in enumerate(p) :
		d[s] += 1
		if d[')'] == d['('] : 
			u = p[:i+1]
			v = p[i+1:]

			if isCorrect(u) :
				return u + uv(v,ans)
			else:
				# 비었거나 더이상 안나눠지면 
				return conversion(u, uv(v,ans))
				
def conversion(u,v) :
	new_u = ''
	for i in range(1,len(u)-1) :
		if u[i] == '(' : new_u += ')'
		else : new_u += '('
	return '(' + v + ')' + new_u

def solution(p):
	answer = ''
	# 이미 올바르면
	if isCorrect(p) or not p:
		answer+=p
		return answer
	
	answer = uv(p,answer)
	return answer 

p = [")()()("] # ((()))

for x in p : 
	print(solution(x))


