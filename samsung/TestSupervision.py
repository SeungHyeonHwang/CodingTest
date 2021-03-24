
def solution(n,a,b,c):
	answer = 0
	for student in a : 
		num = (student - b)
		if num <= 0 :
			continue
		if num%c > 0 :
			answer += int(num/c) + 1
		else :
			answer += int(num/c) 
	return answer + n

n = int(input())
a = map(int, input().split())
b,c = map(int, input().split())
print(solution(n,a,b,c))