# Task 12: Reverse a String Manually

def reverse_text(text):
    reversed_str = ""
    for char in text:
        reversed_str = char + reversed_str
    return reversed_str

# Test Section
if __name__ == "__main__":
    # Test Case 1: Standard word
    txt1 = "function"
    res1 = reverse_text(txt1)
    print(f"Test Case 1: '{txt1}' -> Reversed = '{res1}' (Expected: 'noitcnuf')")
    
    # Test Case 2: Single character string
    txt2 = "a"
    res2 = reverse_text(txt2)
    print(f"Test Case 2: '{txt2}' -> Reversed = '{res2}' (Expected: 'a')")
