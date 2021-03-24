class Solution(object):
	def maxProfit(self, prices):
		"""
		:type prices: List[int]
		:rtype: int
		"""
		# greed, O(N)
		max_profit, min_price = 0, float('inf')
		for price in prices:
			min_price = min(price, min_price)
			profit = price - min_price
			max_profit = max(profit, max_profit)
		return max_profit

prices = [4,2,8,3,5,3,6,10]
#prices = [7,6,4,3,1] # [dp] 0:3, 1:
print(Solution().maxProfit(prices))