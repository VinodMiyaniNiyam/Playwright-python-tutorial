# Task 17: Print Prime Numbers in a Range

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if i * i > n:
            break
        if n % i == 0:
            return False
    return True

def primes_between(start, end):
    primes_list = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes_list.append(num)
            
    # Print the prime numbers
    print(f"Prime numbers between {start} and {end}:")
    for p in primes_list:
        print(p, end=" ")
    print() # New line
    
    return primes_list

# Test Section
if __name__ == "__main__":
    # Test Case 1: Range with primes
    s1, e1 = 10, 20
    res1 = primes_between(s1, e1)
    print(f"Test Case 1 Output: {res1} (Expected: [11, 13, 17, 19])")
    print()
    
    # Test Case 2: Range without primes
    s2, e2 = 8, 10
    res2 = primes_between(s2, e2)
    print(f"Test Case 2 Output: {res2} (Expected: [])")
