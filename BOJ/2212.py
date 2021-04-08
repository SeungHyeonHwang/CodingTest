"""
센서
문제 이해가 안됐던 문제
예외처리로 indexError도 처리해야함.
"""

	
def solution(n,k):
	if k>=n:
		return 0
	sensors.sort()
	gap = []
	for i in range(1,n):
		gap.append(sensors[i]-sensors[i-1])
	gap.sort()
	for i in range(k-1):
		gap.pop(-1)
	return sum(gap)

n = int(input())
k = int(input())
sensors = list(map(int, input().split()))
print(solution(n,k))