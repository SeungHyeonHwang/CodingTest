

import heapq
def solution(jobs):
	answer = []
	q = []
	jobs.sort()
	heapq.heappush(q, [jobs[0][1], jobs[0][0]]) 
	for i in range(1, len(jobs)):
		if jobs[0][1] == jobs[i][1]:
			heapq.heappush(q, [jobs[i][1], jobs[i][0]]) 
		else :
			break
	idx,waiting_time,t = len(q), q[0][1],0
	while q : 
		p = heapq.heappop(q)
		waiting_time += p[0]
		answer.append(abs(waiting_time-p[1]))
		while idx < len(jobs) : 
			if waiting_time >= jobs[idx][0]:
				heapq.heappush(q, [jobs[idx][1], jobs[idx][0]])
				idx+=1
			else :
				break

		if not q and idx < len(jobs) :
			heapq.heappush(q, [jobs[idx][1], jobs[idx][0]])
	print(answer)
	return sum(answer)//len(answer)


jobs =  [[0, 5], [2, 10], [1000, 2]] 
jobs = [[0, 3], [1, 9], [2, 6], [30, 3]]

print(solution(jobs))
# 11, 10, 6