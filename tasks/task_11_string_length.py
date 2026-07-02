# Task 11: Manual String Length

def string_length(text):
    count = 0
    for _ in text:
        count += 1
    return count

# Test Section
if __name__ == "__main__":
    # Test Case 1: Standard string
    txt1 = "Python"
    res1 = string_length(txt1)
    print(f"Test Case 1: '{txt1}' -> Length = {res1} (Expected: 6)")
    
    # Test Case 2: Empty string
    txt2 = ""
    res2 = string_length(txt2)
    print(f"Test Case 2: '{txt2}' -> Length = {res2} (Expected: 0)")
