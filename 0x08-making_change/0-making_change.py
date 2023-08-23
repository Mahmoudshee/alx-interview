#!/usr/bin/python3

def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given amount total.

    Args:
        coins (list[int]): List of coin values.
        total (int): Target total amount.

    Returns:
        int: Fewest number of coins needed to meet the total.
            Returns -1 if total cannot be met.
    """
    # Check if the total amount is 0 or less
    if total <= 0:
        return 0

    # Initialize minimum number of coins needed for each total value
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    # Iterate through each coin value in the list
    for coin in coins:
        # Iterate through each possible total value
        for i in range(coin, total + 1):
            # Calculate the minimum number of coins needed
            dp[i] = min(dp[i], dp[i - coin] + 1)

    # If the minimum number of coins is still infinity,no changes occurs
    if dp[total] == float('inf'):
        return -1

    # Return the minimum number of coins needed to meet the total amount
    return dp[total]

# Test cases


print(makeChange([1, 2, 25], 37))  # Expected output: 7
print(makeChange([1256, 54, 48, 16, 102], 1453))  # Expected output: -1
