class Solution(object):
	def maxSubArray(self, nums):
		inf = -10**5-1
		dp = [inf]*(len(nums)+1)
		dp[0] = nums[0]
		for i in range(1,len(nums)):

			dp[i] = max(nums[i], dp[i-1]+nums[i])
		return max(dp)

nums = [-2]
print(Solution().maxSubArray(nums))