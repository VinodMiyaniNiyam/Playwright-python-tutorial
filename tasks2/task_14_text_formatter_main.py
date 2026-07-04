# Task 14: Text Formatter Module (main file)
# Topics: Modules, string functions

import sys, os
sys.path.insert(0, os.path.dirname(__file__))
import textutils as tu

def run_text_formatter_tests():
    print("=" * 45)
    print("    TEXT FORMATTER MODULE RESULTS")
    print("=" * 45)

    # Test Case 1: Normal sentence
    text1 = "  python   is   a   great   language  "
    print("Test Case 1: Normal Sentence")
    print(f"  Input           : '{text1}'")
    print(f"  Word Count      : {tu.count_words(text1)}")
    print(f"  Vowel Count     : {tu.count_vowels(text1)}")
    print(f"  Reversed        : {tu.reverse_text(text1.strip())}")
    print(f"  Title Case      : {tu.title_case(text1.strip())}")
    print(f"  Extra Spaces    : '{tu.remove_extra_spaces(text1)}'")
    print(f"  Is Palindrome?  : {tu.is_palindrome(text1.strip())}")
    print()

    # Test Case 2: Palindrome check
    text2 = "racecar"
    print("Test Case 2: Palindrome")
    print(f"  '{text2}' -> Is Palindrome? {tu.is_palindrome(text2)}")
    print()

    # Test Case 3: Complex sentence
    text3 = "Never odd or even"
    print("Test Case 3: Palindrome sentence")
    print(f"  '{text3}' -> Is Palindrome? {tu.is_palindrome(text3)}")

    print("=" * 45)

if __name__ == "__main__":
    run_text_formatter_tests()
