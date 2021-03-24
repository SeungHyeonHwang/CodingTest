# 참조
# https://velog.io/@tjdud0123/%EB%8B%A8%EC%96%B4%EB%B3%80%ED%99%98-python

def conversion(curr, words):
	cand = []
	for word in words : 
		diff = [True for x,y in zip(curr, word) if x != y]
		if len(diff) == 1 : 
			cand.append(word)
	return cand

from collections import deque
def solution(begin, target, words):

	visited = set(begin)
	q = deque([[begin, 0]])
	
	while q : 
		curr, cnt = q.popleft()
		if curr == target : 
			return cnt
		
		for word in conversion(curr, words) :
			if word not in visited :
				q.append([word, cnt+1])
				print(q)
				visited.add(word)
	return 0 
	
begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]
print(solution(begin, target, words))