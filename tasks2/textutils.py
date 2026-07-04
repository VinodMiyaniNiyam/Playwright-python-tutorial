# Task 14: Text Formatter Module - textutils.py
# Topics: Modules, string functions

def count_words(text):
    words = text.strip().split()
    return len(words)

def count_vowels(text):
    count = 0
    for ch in text.lower():
        if ch in "aeiou":
            count += 1
    return count

def reverse_text(text):
    return text[::-1]

def title_case(text):
    return text.title()

def remove_extra_spaces(text):
    words = text.split()
    return " ".join(words)

def is_palindrome(text):
    cleaned = "".join(ch.lower() for ch in text if ch.isalnum())
    return cleaned == cleaned[::-1]
