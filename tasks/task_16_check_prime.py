# Task 16: Check Prime Using Function

def is_prime(n):
    if n <= 1:
        return False
        
    # Check divisibility up to i * i <= n manually without math library
    for i in range(2, n):
        if i * i > n:
            break
        if n % i == 0:
            return False
            
    return True

# Test Section
if __name__ == "__main__":
    # Test Case 1: Prime number
    num1 = 29
    res1 = is_prime(num1)
    print(f"Test Case 1: Is {num1} prime? {res1} (Expected: True)")
    
    # Test Case 2: Composite number
    num2 = 4
    res2 = is_prime(num2)
    print(f"Test Case 2: Is {num2} prime? {res2} (Expected: False)")
    
    # Test Case 3: Edge case 1
    num3 = 1
    res3 = is_prime(num3)
    print(f"Test Case 3: Is {num3} prime? {res3} (Expected: False)")
