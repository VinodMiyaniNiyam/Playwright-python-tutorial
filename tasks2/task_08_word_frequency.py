# Task 8: Word Frequency Counter
# Topics: String functions, dictionaries, loops

def clean_text(text):
    punctuation = ".,?!;:'\"-()[]{}\\/"
    cleaned = ""
    for char in text.lower():
        if char not in punctuation:
            cleaned += char
    return cleaned

def count_words(text):
    cleaned = clean_text(text)
    words = cleaned.split()
    freq = {}
    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    return freq

def most_frequent_word(freq):
    top_word = None
    top_count = 0
    for word, count in freq.items():
        if count > top_count:
            top_count = count
            top_word = word
    return top_word, top_count

def print_word_frequency(freq):
    print("=" * 35)
    print("    WORD FREQUENCY REPORT")
    print("=" * 35)
    # Print in alphabetical order
    for word in sorted(freq.keys()):
        print(f"  {word:<20} : {freq[word]}")
    print("=" * 35)

# Test Section
if __name__ == "__main__":
    # Test Case 1: Normal paragraph
    text1 = "Python is great. Python is easy. Python is fun!"
    freq1 = count_words(text1)
    print("Test Case 1:")
    print_word_frequency(freq1)
    top, count = most_frequent_word(freq1)
    print(f"  Most frequent word: '{top}' ({count} times)")
    print()

    # Test Case 2: Mixed punctuation
    text2 = "Hello, world! Hello again. World is beautiful."
    freq2 = count_words(text2)
    print("Test Case 2:")
    print_word_frequency(freq2)
    print()

    # Test Case 3: Single word repeated
    text3 = "yes yes yes no no"
    freq3 = count_words(text3)
    print("Test Case 3:")
    print_word_frequency(freq3)
