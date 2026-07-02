# Task 4: Count Vowels and Consonants

def count_letters(text):
    vowels_count = 0
    consonants_count = 0
    vowels_chars = "aeiouAEIOU"
    
    for char in text:
        # Check if alphabetical manually using comparison
        if ('a' <= char <= 'z') or ('A' <= char <= 'Z'):
            # Check if vowel manually
            is_vowel = False
            for v in vowels_chars:
                if char == v:
                    is_vowel = True
                    break
            
            if is_vowel:
                vowels_count += 1
            else:
                consonants_count += 1
                
    return f"vowels: {vowels_count}, consonants: {consonants_count}"

# Test Section
if __name__ == "__main__":
    # Test Case 1: Standard string
    txt1 = "Python Class"
    res1 = count_letters(txt1)
    print(f"Test Case 1: '{txt1}' -> {res1} (Expected: vowels: 2, consonants: 9)")
    
    # Test Case 2: String with numbers and special characters
    txt2 = "A1b! #c"
    res2 = count_letters(txt2)
    print(f"Test Case 2: '{txt2}' -> {res2} (Expected: vowels: 1, consonants: 2)")
