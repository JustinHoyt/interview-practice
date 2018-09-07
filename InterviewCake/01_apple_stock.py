def pick_stock_dynamic(prices):
    size = len(prices)
    high_ranges = {(size-1, size-1): prices[-1]}
    for i in range(size-2, -1, -1):
        high_ranges[(i, size-1)] = max(high_ranges[(i+1, size-1)], prices[i])
    best_sell = float('-inf')
    for i in range(size-1):
        temp_sell = high_ranges[(i+1, size-1)] - prices[i]
        best_sell = max(best_sell, temp_sell)
    return best_sell

prices = [10, 7, 5, 8, 11, 9]
print(pick_stock_dynamic(prices))

def pick_stock_greedy(prices):
    size = len(prices)
    min_price = float('inf')
    best_sell = float('-inf')
    for i in range(1, size-1):
        min_price = min(min_price, prices[i-1])
        temp_sell = prices[i] - min_price
        best_sell = max(best_sell, temp_sell)
    return best_sell

prices = [10, 7, 5, 8, 11, 9]
print(pick_stock_greedy(prices))
