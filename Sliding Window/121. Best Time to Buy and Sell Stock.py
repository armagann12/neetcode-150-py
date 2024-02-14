# My solution
# Using sliding window
# Startig from the start of the array and if left pointer is bigger than right
# We can say there is a smaller price we can buy so we move to l to r position
# And every tine we move r 1 more and also calculate max
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        l = 0
        r = 1

        while r < len(prices):
            res = max(res, prices[r] - prices[l])
            if prices[l] > prices[r]:
                l = r
            r += 1
        return res
        