"""
Max Profit with One Transaction.

Given a list of a stock's price in the ith day, calculate the max profit if
you can only buy one stock and sell one stock.

EXAMPLE:
[7,1,5,3,6,4] -> 5
"""

print()

# METHOD 1 - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
print('METHOD 1')


def max_profit_one_transaction(prices):
    """
    Calculate the max profit in prices with one transaction.

    LOGIC:
    Loop the list and keep updating the max profit

    INPUT:
    prices: a list of prices in the ith day

    OUTPUT:
    The max profit from buying and selling the stock on time
    """
    buy_price = float("inf")
    result = 0

    for i in prices:
        buy_price = min(buy_price, i)
        result = max(result, i-buy_price)

    return result


# TEST CASES
TEST_A = [7, 1, 5, 3, 6, 4]

RESULT_A = max_profit_one_transaction(TEST_A)

CORRECT_A = 5

print("Testing A: ", end="")
print("OK" if RESULT_A == CORRECT_A
      else "FAIL (" + str(RESULT_A) + " vs " + str(CORRECT_A) + ")")

print()
