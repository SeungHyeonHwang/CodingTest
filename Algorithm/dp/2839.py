# 백준 : 2839번
# 설탕배달






"""

dp[1] = 3,5
dp[2] = 1,1
dp[3] = 1,2
dp[4] = 1,3 / 2,2
dp[5] = 1,4 / 2,3 
"""

n = int(input())

dp = [5001]*5001

dp[3] =1 
dp[5] =1

for i in range(6,n+1):
  if dp[i-3] != 5001:
    dp[i] = dp[i-3]+1
  if dp[i-5] != 5001:
    dp[i] = min(dp[i], dp[i-5]+1)
    
if dp[n] == 5001:
  print(-1)
else :
  print(dp[n])