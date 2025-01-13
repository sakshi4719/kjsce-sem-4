def knapsack(weights, values, capacity):
    n = len(weights)
    # Create a table to store the maximum value that can be obtained
    # for each combination of items and capacity
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    # Fill the dp table
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            # If the current item's weight is greater than the current capacity,
            # we can't include it in the knapsack
            if weights[i - 1] > w:
                dp[i][w] = dp[i - 1][w]
            else:
                # Otherwise, we have two choices: include the current item
                # or exclude it
                dp[i][w] = max(dp[i - 1][w], values[i - 1] + dp[i - 1][w - weights[i - 1]])

    # The maximum value is stored in the bottom-right cell of the dp table
    return dp[n][capacity]

# Example usage:
weights = [1,3,4,6]
values = [4,5,7,10]
capacity = 9
print("Maximum value:", knapsack(weights, values, capacity))
