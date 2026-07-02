# Task 6: Check Strong Password

def is_strong_password(password):
    length = 0
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    special_chars = '!@#$%^&*()-_=+[]{}|;:\'",.<>/?\\`~'
    
    for char in password:
        length += 1
        if 'A' <= char <= 'Z':
            has_upper = True
        elif 'a' <= char <= 'z':
            has_lower = True
        elif '0' <= char <= '9':
            has_digit = True
        else:
            # Check if it is a special character manually
            for s in special_chars:
                if char == s:
                    has_special = True
                    break
                    
    return length >= 8 and has_upper and has_lower and has_digit and has_special

# Test Section
if __name__ == "__main__":
    # Test Case 1: Valid strong password
    pwd1 = "Abc@1234"
    res1 = is_strong_password(pwd1)
    print(f"Test Case 1: '{pwd1}' -> {res1} (Expected: True)")
    
    # Test Case 2: Weak password (no uppercase or special)
    pwd2 = "password123"
    res2 = is_strong_password(pwd2)
    print(f"Test Case 2: '{pwd2}' -> {res2} (Expected: False)")
    
    # Test Case 3: Weak password (too short)
    pwd3 = "A@1b"
    res3 = is_strong_password(pwd3)
    print(f"Test Case 3: '{pwd3}' -> {res3} (Expected: False)")
