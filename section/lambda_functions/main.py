prices = [210, 0, -891, 432, 256]

apply_tax = lambda x: max(x, 0) * 0.87   # Deducting 13% tax

final_prices = [apply_tax(p) for p in prices]

# Testing the result
print(final_prices)