




def solution(n,grades):
	grades.sort(key=lambda x : x[0])
	answer=1
	minv = grades[0][1]
	for i in range(1, len(grades)):
		if (minv > grades[i][1]):
			answer+=1
			minv=grades[i][1]
	return answer

test_case = int(input())
for _ in range(test_case):
	n = int(input())
	grades = [list(map(int, input().split())) for _ in range(n)]
	print(solution(n,grades))