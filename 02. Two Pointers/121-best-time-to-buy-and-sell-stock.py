# Leetcode 121

from typing import List


def maxProfit(prices: List[int]) -> int:
    # so basically we take two pointers
    left, right = 0, 1
    # we need value to record the current max profit
    maxProfit = 0
    # while right is not at the end of prices
    while right < len(prices):
        # if prices left is lower than prices right
        # in other words, past price is cheaper than current price
        if prices[left] < prices[right]:
            # calculate the profit
            profit = prices[right] - prices[left]
            # then record the profit by comparing with the current profit
            maxProfit = max(maxProfit, profit)
        # else, meaning current price is lower than past price
        else:
            # we want to buy the current price to be the new past price
            left = right
        # and move the right to next, meaning time flows ->
        right += 1
    # and the return the max profit. Voila!
    return maxProfit



# Testing
prices = [7, 1, 5, 3, 6, 4, 21]

print(maxProfit(prices))