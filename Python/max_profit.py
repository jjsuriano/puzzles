# DESCRIPTION:
# Given a list of a stock's price in the ith day, calculate the max profit if
# you can buy one stock and sell one stock as many times you want, but you have
# to buy and sell one stock at time.

# EXAMPLE:
# [10, 22, 5, 75, 65, 80] -> 97

# INPUT:
# A list of prices in the ith day

# OUTPUT:
# The max profit from buying and selling the stock

prices = [10, 22, 10, 5, 45, 78, 65, 80]
print()

# METHOD 1 - - - - -
print('METHOD 1')

# LOGIC:
# Add the profit if the price increases, if the price decreases do nothing

maxProfit = 0

for i in range(1, len(prices)):
    if prices[i-1] < prices[i]:
        maxProfit += prices[i] - prices[i-1]

print(f"The max profit you can make is: ${maxProfit}")
print()