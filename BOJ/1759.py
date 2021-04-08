


from itertools import combinations
def solution(l,c):
	alphabet = list('abcdefghijklmnopqrstuvwxyz')
	answer_set = set()	

	for comb in combinations(strings, l):
		count = [0,0]
		for c in comb :
			if c in ['a','e','i','o','u']:
				count[0]+=1
			else :
				count[1]+=1
		if count[0] > 0 and count[1] > 1 :
			answer_set.add(''.join(sorted(comb)))
	answer = sorted(answer_set)
	for ans in answer :
		print(ans)
l,c = map(int, input().split())
strings = list(map(str, input().split()))
solution(l,c)