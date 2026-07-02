# Task 7: Second Largest Number in a List

def second_largest(numbers):
    # Find list length manually
    length = 0
    for _ in numbers:
        length += 1
        
    if length < 2:
        return None
        
    # Find the maximum value
    largest = None
    for num in numbers:
        if largest is None or num > largest:
            largest = num
            
    # Find the second largest (must be strictly less than the largest)
    sec_largest = None
    for num in numbers:
        if num != largest:
            if sec_largest is None or num > sec_largest:
                sec_largest = num
                
    return sec_largest

# Test Section
if __name__ == "__main__":
    # Test Case 1: Standard list with duplicate maximums
    nums1 = [10, 40, 20, 40, 30]
    res1 = second_largest(nums1)
    print(f"Test Case 1: {nums1} -> Second Largest = {res1} (Expected: 30)")
    
    # Test Case 2: List with identical elements
    nums2 = [5, 5, 5]
    res2 = second_largest(nums2)
    print(f"Test Case 2: {nums2} -> Second Largest = {res2} (Expected: None)")
    
    # Test Case 3: List with 1 element
    nums3 = [10]
    res3 = second_largest(nums3)
    print(f"Test Case 3: {nums3} -> Second Largest = {res3} (Expected: None)")
