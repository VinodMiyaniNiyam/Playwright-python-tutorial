# Task 13: Check Palindrome String

def is_text_palindrome(text):
    # Step 1: Clean spaces and convert uppercase to lowercase manually
    cleaned = ""
    for char in text:
        if char != ' ':
            # If uppercase, convert to lowercase using ASCII offset (32)
            if 'A' <= char <= 'Z':
                cleaned += chr(ord(char) + 32)
            else:
                cleaned += char
                
    # Step 2: Calculate length manually
    length = 0
    for _ in cleaned:
        length += 1
        
    # Step 3: Compare characters from start and end
    for i in range(length // 2):
        if cleaned[i] != cleaned[length - 1 - i]:
            return False
            
    return True

# Test Section
if __name__ == "__main__":
    # Test Case 1: Palindrome sentence with mixed case and spaces
    txt1 = "Never odd or even"
    res1 = is_text_palindrome(txt1)
    print(f"Test Case 1: '{txt1}' -> Is Palindrome? {res1} (Expected: True)")
    
    # Test Case 2: Non-palindrome word
    txt2 = "hello"
    res2 = is_text_palindrome(txt2)
    print(f"Test Case 2: '{txt2}' -> Is Palindrome? {res2} (Expected: False)")
