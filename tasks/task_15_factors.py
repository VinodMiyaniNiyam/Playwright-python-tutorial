# Task 15: Find All Factors

def factors(n):
    if n <= 0:
        return []
        
    factors_list = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors_list.append(i)
            
    return factors_list

# Test Section
if __name__ == "__main__":
    # Test Case 1: Factors of 12
    num1 = 12
    res1 = factors(num1)
    print(f"Test Case 1: Factors of {num1} -> {res1} (Expected: [1, 2, 3, 4, 6, 12])")
    
    # Test Case 2: Factors of 7 (Prime number)
    num2 = 7
    res2 = factors(num2)
    print(f"Test Case 2: Factors of {num2} -> {res2} (Expected: [1, 7])")
