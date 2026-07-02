# Task 8: Count Positive, Negative and Zero Values

def count_numbers(numbers):
    pos_count = 0
    neg_count = 0
    zero_count = 0
    
    for num in numbers:
        if num > 0:
            pos_count += 1
        elif num < 0:
            neg_count += 1
        else:
            zero_count += 1
            
    return f"positive: {pos_count}, negative: {neg_count}, zero: {zero_count}"

# Test Section
if __name__ == "__main__":
    # Test Case 1: Normal list with mixed values
    nums1 = [5, -2, 0, 7, -9, 0]
    res1 = count_numbers(nums1)
    print(f"Test Case 1: {nums1} -> {res1} (Expected: positive: 2, negative: 2, zero: 2)")
    
    # Test Case 2: Empty list
    nums2 = []
    res2 = count_numbers(nums2)
    print(f"Test Case 2: {nums2} -> {res2} (Expected: positive: 0, negative: 0, zero: 0)")
