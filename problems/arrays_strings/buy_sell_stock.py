# 121. Best Time to Buy and Sell Stock
# Given an array prices where prices[i] is the price of a given stock on the ith day,
# return the maximum profit you can achieve from this transaction.
# If you cannot achieve any profit, return 0.
# You must buy before you sell.

from typing import List

def maxProfit(prices: List[int]) -> int:
    max_value=0
    for j in range(len(prices)-1):
        for i in range(j+1,len(prices)-1):
            if prices[i]>prices[j]:
                max_value=max((prices[i]-prices[j]),max_value)
    return max_value

if __name__ == "__main__":
    prices = [7,1,5,3,6,4]
    print(maxProfit(prices))  # Output: 5