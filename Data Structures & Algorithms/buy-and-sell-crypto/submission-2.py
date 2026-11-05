class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        j = i + 1
        maxProfit = 0
        while j < len(prices):
            if prices[i] < prices[j]:
                total = prices[j] - prices[i]
                maxProfit = max(maxProfit, total)
            else:
                i = j
            j += 1
        return maxProfit