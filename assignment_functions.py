"""
Python Functions Practical Assignment
Moderate Level - Branching, Loops and User-Defined Functions

This module implements the solutions to the assignment questions strictly following
the guidelines:
- No importing of any libraries/modules in this file.
- Plain branching and looping statements only.
- No built-in shortcuts like sum(), max(), min(), sorted(), reversed(), bin(), pow(),
  any(), all(), split(), join(), count(), find(), replace(), etc.
"""

# Helper to check if a character exists in a string manually
def _char_in_string(c: str, s: str) -> bool:
    for x in s:
        if x == c:
            return True
    return False

# Helper to calculate length of a sequence/string/list manually
def _len_manual(seq) -> int:
    count = 0
    for _ in seq:
        count += 1
    return count

# 1. Student Grade Calculator
def calculate_grade(marks) -> str:
    if not isinstance(marks, (int, float)):
        return "Invalid"
    if marks < 0 or marks > 100:
        return "Invalid"
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 40:
        return "D"
    else:
        return "F"

# 2. Electricity Bill Calculator
def electricity_bill(units) -> float:
    if units < 0:
        return 0.0
    bill = 0.0
    if units <= 100:
        bill = units * 5.0
    elif units <= 200:
        bill = (100 * 5.0) + ((units - 100) * 7.0)
    else:
        bill = (100 * 5.0) + (100 * 7.0) + ((units - 200) * 10.0)
    return bill

# 3. Simple ATM Withdrawal
def atm_withdraw(balance, amount):
    if amount <= 0:
        return "Amount must be positive"
    if amount % 100 != 0:
        return "Amount must be a multiple of 100"
    if amount > balance:
        return "Insufficient balance"
    return balance - amount

# 4. Count Vowels and Consonants
def count_letters(text: str) -> dict:
    vowels_count = 0
    consonants_count = 0
    vowels_chars = "aeiouAEIOU"
    
    for char in text:
        # Check if alphabetical manually
        if ('a' <= char <= 'z') or ('A' <= char <= 'Z'):
            if _char_in_string(char, vowels_chars):
                vowels_count += 1
            else:
                consonants_count += 1
                
    return {"vowels": vowels_count, "consonants": consonants_count}

# 5. Remove Duplicate Characters
def remove_duplicates(text: str) -> str:
    result = ""
    for char in text:
        if not _char_in_string(char, result):
            result += char
    return result

# 6. Check Strong Password
def is_strong_password(password: str) -> bool:
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
            if _char_in_string(char, special_chars):
                has_special = True
                
    return length >= 8 and has_upper and has_lower and has_digit and has_special

# 7. Second Largest Number in a List
def second_largest(numbers: list):
    length = _len_manual(numbers)
    if length < 2:
        return None
        
    largest = None
    for num in numbers:
        if largest is None or num > largest:
            largest = num
            
    sec_largest = None
    for num in numbers:
        if num != largest:
            if sec_largest is None or num > sec_largest:
                sec_largest = num
                
    return sec_largest

# 8. Count Positive, Negative and Zero Values
def count_numbers(numbers: list) -> dict:
    pos_count = 0
    neg_count = 0
    zero_count = 0
    for num in numbers:
        if num > 0:
            pos_count += 1
        elif num < 0:
            neg_count += 1
        else:
            zero_count += 1
    return {"positive": pos_count, "negative": neg_count, "zero": zero_count}

# 9. List Average Without sum()
def average(numbers: list):
    count = 0
    total = 0.0
    for num in numbers:
        count += 1
        total += num
    if count == 0:
        return "Invalid"
    return total / count

# 10. Search Element Manually
def search_item(numbers: list, target) -> int:
    idx = 0
    for num in numbers:
        if num == target:
            return idx
        idx += 1
    return -1

# 11. Manual String Length
def string_length(text: str) -> int:
    count = 0
    for _ in text:
        count += 1
    return count

# 12. Reverse a String Manually
def reverse_text(text: str) -> str:
    rev = ""
    for char in text:
        rev = char + rev
    return rev

# 13. Check Palindrome String
def is_text_palindrome(text: str) -> bool:
    cleaned = ""
    for char in text:
        if char != ' ':
            # Convert uppercase to lowercase manually
            if 'A' <= char <= 'Z':
                cleaned += chr(ord(char) + 32)
            else:
                cleaned += char
                
    length = _len_manual(cleaned)
    for i in range(length // 2):
        if cleaned[i] != cleaned[length - 1 - i]:
            return False
    return True

# 14. Print Right Triangle Pattern
def print_triangle(n: int) -> str:
    result = ""
    for i in range(1, n + 1):
        row = ""
        for _ in range(i):
            row += "*"
        print(row)
        result += row
        if i < n:
            result += "\n"
    return result

# 15. Find All Factors
def factors(n: int) -> list:
    if n <= 0:
        return []
    res = []
    for i in range(1, n + 1):
        if n % i == 0:
            res.append(i)
    return res

# 16. Check Prime Using Function
def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    for i in range(2, n):
        if i * i > n:
            break
        if n % i == 0:
            return False
    return True

# 17. Print Prime Numbers in a Range
def primes_between(start: int, end: int) -> list:
    res = []
    for num in range(start, end + 1):
        if is_prime(num):
            res.append(num)
    return res

# 18. Simple Calculator Function
def calculator(a, b, operator: str):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        if b == 0:
            return "Error: Division by zero"
        return a / b
    elif operator == '%':
        if b == 0:
            return "Error: Division by zero"
        return a % b
    else:
        return "Error: Invalid operator"

# 19. Employee Salary Calculation
def net_salary(basic: float) -> float:
    if basic < 0:
        return 0.0
    hra = 0.20 * basic
    da = 0.10 * basic
    gross = basic + hra + da
    tax = 0.05 * gross
    net = gross - tax
    return net

# 20. Shopping Cart Total
def cart_total(prices: list, quantities: list) -> float:
    len_p = _len_manual(prices)
    total = 0.0
    for i in range(len_p):
        total += prices[i] * quantities[i]
        
    if total > 5000:
        total = total * 0.90 # 10% discount
    return total

# --- Optional Challenge ---
# Menu-driven marks management functions using only lists (no dicts, no imports)

def add_student(names_list: list, marks_list: list, name: str, mark: float) -> bool:
    names_list.append(name)
    marks_list.append(mark)
    return True

def show_students(names_list: list, marks_list: list) -> str:
    length = _len_manual(names_list)
    if length == 0:
        return "No students found."
    
    result = "Student Records:\n"
    for i in range(length):
        result += f"- {names_list[i]}: {marks_list[i]}"
        if i < length - 1:
            result += "\n"
    return result

def find_highest_marks(names_list: list, marks_list: list) -> tuple:
    length = _len_manual(marks_list)
    if length == 0:
        return None, None
        
    highest_idx = 0
    highest_val = marks_list[0]
    for i in range(1, length):
        if marks_list[i] > highest_val:
            highest_val = marks_list[i]
            highest_idx = i
            
    return names_list[highest_idx], highest_val

def calculate_class_average(marks_list: list) -> float:
    length = _len_manual(marks_list)
    if length == 0:
        return 0.0
    total = 0.0
    for mark in marks_list:
        total += mark
    return total / length

def _to_lower(s: str) -> str:
    res = ""
    for char in s:
        if 'A' <= char <= 'Z':
            res += chr(ord(char) + 32)
        else:
            res += char
    return res

def search_student(names_list: list, marks_list: list, name: str) -> int:
    length = _len_manual(names_list)
    search_name_lower = _to_lower(name)
    for i in range(length):
        if _to_lower(names_list[i]) == search_name_lower:
            return i
    return -1
