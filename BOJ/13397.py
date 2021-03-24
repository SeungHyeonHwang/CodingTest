"""
구간 나누기 2
완전탐색시 시간초과
binary search 

"""


def binarySearch(x):
	cnt = 1
	max_num = min_num = arr[0]
	
	for i in range(1, len(arr)):
		max_num = max(max_num, arr[i])
		min_num = min(min_num, arr[i])

		if max_num - min_num > x :
			max_num = arr[i]
			min_num = arr[i]
			cnt+=1

	return cnt



def solution(n,m):
	start, end = 0, max(arr) # mid 는 max(arr) 보다 작음
	result = 0
	while start <= end :
		mid = (start + end)//2
		
		temp = binarySearch(mid)
		print('mid : ',mid, temp) 
		if temp <= m :
			end = mid-1
			result = mid
		else :
			start = mid+1
		print(start, end)
	return result   

n,m = map(int, input().split())
arr = list(map(int, input().split()))
print(solution(n,m))

