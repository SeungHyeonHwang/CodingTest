

def solution(ps):

	VPS = {'(':0, ')':0}
	for s in ps : 
		VPS[s]+=1
		if VPS[')'] > VPS['(']:
			return 'NO'
	if VPS['('] == VPS[')'] :
		return 'YES'
	return 'NO'

test_case = int(input())
for t in range(test_case) : 
	ps = list(map(str, input()))
	print(solution(ps))