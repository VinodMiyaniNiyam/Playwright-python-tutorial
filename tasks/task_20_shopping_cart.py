# Task 20: Shopping Cart Total

def cart_total(prices, quantities):
    # Calculate list length manually
    length = 0
    for _ in prices:
        length += 1
        
    total = 0.0
    for i in range(length):
        total += prices[i] * quantities[i]
        
    # Apply 10% discount if total is strictly greater than 5000
    if total > 5000:
        total = total * 0.90
        
    return total

# Test Section
if __name__ == "__main__":
    # Test Case 1: Total greater than 5000 (discount applies)
    prices1 = [1000, 500, 200]
    quants1 = [3, 4, 5]
    res1 = cart_total(prices1, quants1)
    print(f"Test Case 1: Prices={prices1}, Quantities={quants1} -> Total = {res1} (Expected: 5400.0)")
    
    # Test Case 2: Total less than 5000 (no discount)
    prices2 = [100, 200]
    quants2 = [2, 3]
    res2 = cart_total(prices2, quants2)
    print(f"Test Case 2: Prices={prices2}, Quantities={quants2} -> Total = {res2} (Expected: 800.0)")
