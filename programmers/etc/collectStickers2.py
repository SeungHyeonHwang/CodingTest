# 스티커 모으기 (2)
# https://programmers.co.kr/learn/courses/30/lessons/12971
# 풀이 참조 DP 

def solution(sticker):

	if len(sticker) < 4:
		return max(sticker)
	dp = [0]*len(sticker)
	dp[0] = sticker[0]
	dp[1] = dp[0]

	for i in range(2,len(sticker)-1):
		dp[i] = max(dp[i-1], dp[i-2] + sticker[i])
	value = max(dp)

	dp = [0]*len(sticker)
	dp[0] = 0
	dp[1] = sticker[1]

	for i in range(2,len(sticker)):
		dp[i] = max(dp[i-1], dp[i-2] + sticker[i])

	return max(value, max(dp))

sticker = [14,1,2]
print(solution(sticker))