# Task 10: Search Element Manually

def search_item(numbers, target):
    idx = 0
    for num in numbers:
        if num == target:
            return idx
        idx += 1
    return -1

# Test Section
if __name__ == "__main__":
    # Test Case 1: Search element present multiple times (first index returned)
    nums1, target1 = [4, 8, 1, 8], 8
    res1 = search_item(nums1, target1)
    print(f"Test Case 1: Search {target1} in {nums1} -> Index = {res1} (Expected: 1)")
    
    # Test Case 2: Search element not present
    nums2, target2 = [4, 8, 1, 8], 10
    res2 = search_item(nums2, target2)
    print(f"Test Case 2: Search {target2} in {nums2} -> Index = {res2} (Expected: -1)")
