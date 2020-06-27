# DESCRIPTION:
# Given a list of a stock's price in the ith day, calculate the max profit if
# you can only buy one stock and sell one stock.

# EXAMPLE:
# [7,1,5,3,6,4] -> 5

# INPUT:
# A list of prices in the ith day

# OUTPUT:
# The max profit from buying and selling the stock

prices = [7,1,5,3,6,4]
print()

# METHOD 1 - - - - -
print('METHOD 1')

# LOGIC:
# Loop the list and keep updating the max profit

buy_price = float("inf")
max_profit = 0

for i in prices:
    buy_price = min(buy_price, i)
    max_profit = max(max_profit, i-buy_price)

print('The max profit you can do is: ${}.'.format(max_profit))
print()