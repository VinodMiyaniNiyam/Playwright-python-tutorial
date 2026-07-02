# Task 5: Remove Duplicate Characters

def remove_duplicates(text):
    result = ""
    for char in text:
        # Check if character is already in result manually
        already_exists = False
        for r_char in result:
            if char == r_char:
                already_exists = True
                break
        
        if not already_exists:
            result += char
            
    return result

# Test Section
if __name__ == "__main__":
    # Test Case 1: Standard lowercase word
    txt1 = "programming"
    res1 = remove_duplicates(txt1)
    print(f"Test Case 1: '{txt1}' -> '{res1}' (Expected: 'progamin')")
    
    # Test Case 2: Mix case with spaces
    txt2 = "Hello World"
    res2 = remove_duplicates(txt2)
    print(f"Test Case 2: '{txt2}' -> '{res2}' (Expected: 'Helo Wrd')")
