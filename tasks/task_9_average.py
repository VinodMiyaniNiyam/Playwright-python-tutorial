# Task 9: List Average Without sum()

def average(numbers):
    total = 0.0
    count = 0
    
    for num in numbers:
        total += num
        count += 1
        
    if count == 0:
        return "Invalid"
        
    return total / count

# Test Section
if __name__ == "__main__":
    # Test Case 1: Valid list
    nums1 = [10, 20, 30, 40]
    res1 = average(nums1)
    print(f"Test Case 1: {nums1} -> Average = {res1} (Expected: 25.0)")
    
    # Test Case 2: Empty list
    nums2 = []
    res2 = average(nums2)
    print(f"Test Case 2: {nums2} -> Average = {res2} (Expected: Invalid)")
