"""
줄어들지 않아
dp, 규칙을 찾아 해결
  n = 1  2  3 
1    1   9  45    
2    1   8  36
3
4
.
.   1   3   6
8   1   2   3      #   8,    88,89,   888,889,899 
9   1   1   1      #    9,     99,        999

1차원 dp 테이블은 n번 누적됨
dp 인덱스 1은 9로 만들수 있는 경우의수, 즉 뒤집어야함.

ex)
n이 3일때, 1을 만드는 경우의 수는 dp[1] = 9 + 36 = 45 임.
"""


def solution(n):
	dp = [0]*10
	dp[0]=1
	for i in range(n):
		for j in range(1,10):
			dp[j] = dp[j] + dp[j-1] 
	return sum(dp)


t = int(input())
for _ in range(t):
	n = int(input())
	print(solution(n))
