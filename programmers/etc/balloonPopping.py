
def solution(a):
	answer = 0
	# 3이하면 어떤 경우라도 가능
	if len(a) < 4 :
		return len(a)
	
	minIdx = a.index(min(a))
	lmin = a[0]
	rest = list(reversed(a[minIdx+1:]))
	if minIdx != len(a)-1 :
		rmin = rest[0]

	# min 값이 오른쪽에 있을 때, 나는 내 왼쪽 중에 가장 작아야함
	for i in range(1, minIdx) :
		if i < minIdx :
			if a[i] <= lmin : 
				lmin = a[i]
				answer+=1
	# 반대로 뒤집어서 똑같이 생각 
	for i in range(1,len(rest)) :
			if rest[i] <= rmin : 
				rmin = rest[i]
				answer+=1
	return answer+2 if minIdx == 0 or minIdx == len(a)-1 else answer+3

print(solution([-55,3,2,4,-100]))
# -16, -92, -71, -68, -61, -33
# 27, -92, -71, -68, -61, -33
# 8 9 6 5 10 -1 -2
# 5 4 3 2 0 10 6 7 9 
