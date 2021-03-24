

def solution(s):
	dictionary = {}

	for a in s:
		if a not in dictionary.keys():
			dictionary[a] = 1
		else :
			del dictionary[a]
	if not dictionary :
		return "Good"
	else : 
		return ''.join(sorted(dictionary.keys()))

string = [
			"xxyyzz",
			"yc",
			"aaaab",
			"bca",
			"ppzqq",
			"qnwerrewmq"
			]
T = int(input())

for test_case in range(1, T + 1):
	print('#%d %s'%(test_case, solution(input())))