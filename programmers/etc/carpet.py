

def solution(brown, yellow):
	answer = []
	# 면적
	area = brown + yellow 
	cands = set()
	# yellow 있으려면 한변 최소 3이상
	for num in range(3,(area//3)+1):
		# 나눠떨어지면
		if area%num == 0 :
			n = (area//num, num) if area//num >= num else (num, area//num)
			cands.add(n)
	# 후보군에서 옐로우 면적이랑 같으면 정답
	for cand in cands:
		if (cand[0]-2)*(cand[1]-2) == yellow:
			return [cand[0], cand[1]]
		for i in graph[now]:
			

brown = 8
yellow = 1
print(solution(brown, yellow))