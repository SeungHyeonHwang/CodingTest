"""
import math
n = int(input())
a = list(map(int, (input().split(' '))))
b,c = map(int, input().split(' '))

total_num = 0
for i in range(n):
	if a[i]-b <= 0 :
		continue
	elif  (a[i]-b)-c < 0 :
		total_num+=1
	else : 
		total_num+=math.ceil((a[i]-b)/c)
print(total_num+n)
"""

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