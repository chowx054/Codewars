class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        left, right = 0, 1 #right must be greater than left
        res = 0

        while right < len(prices):

            if prices[right] > prices[left]: #then we have a profit
                profit = prices[right] - prices[left]
                res = max(profit, res)
            else:
                left = right #left equals to the last right (move right)

            right += 1
        
        return res