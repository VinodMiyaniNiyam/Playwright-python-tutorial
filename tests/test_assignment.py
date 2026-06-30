import pytest
import assignment_functions as af

# 1. Student Grade Calculator Tests
@pytest.mark.parametrize("marks, expected", [
    (95, "A"),
    (82, "B"),
    (67, "C"),
    (50, "D"),
    (35, "F"),
    (105, "Invalid"),
    (-5, "Invalid"),
    ("abc", "Invalid")
])
def test_calculate_grade(marks, expected):
    assert af.calculate_grade(marks) == expected

# 2. Electricity Bill Calculator Tests
@pytest.mark.parametrize("units, expected", [
    (50, 250.0),
    (150, 850.0),
    (250, 1700.0),
    (-10, 0.0)
])
def test_electricity_bill(units, expected):
    assert af.electricity_bill(units) == expected

# 3. Simple ATM Withdrawal Tests
@pytest.mark.parametrize("balance, amount, expected", [
    (5000, 1200, 3800),
    (5000, -100, "Amount must be positive"),
    (5000, 1250, "Amount must be a multiple of 100"),
    (1000, 1500, "Insufficient balance")
])
def test_atm_withdraw(balance, amount, expected):
    assert af.atm_withdraw(balance, amount) == expected

# 4. Count Vowels and Consonants Tests
@pytest.mark.parametrize("text, expected", [
    ("Python Class", {"vowels": 2, "consonants": 9}),
    ("A1b!", {"vowels": 1, "consonants": 1})
])
def test_count_letters(text, expected):
    assert af.count_letters(text) == expected

# 5. Remove Duplicate Characters Tests
@pytest.mark.parametrize("text, expected", [
    ("programming", "progamin"),
    ("Hello World", "Helo Wrd")
])
def test_remove_duplicates(text, expected):
    assert af.remove_duplicates(text) == expected

# 6. Check Strong Password Tests
@pytest.mark.parametrize("password, expected", [
    ("Abc@1234", True),
    ("password123", False),
    ("A@1bc", False)
])
def test_is_strong_password(password, expected):
    assert af.is_strong_password(password) == expected

# 7. Second Largest Number in a List Tests
@pytest.mark.parametrize("numbers, expected", [
    ([10, 40, 20, 40, 30], 30),
    ([5, 5, 5], None),
    ([10], None)
])
def test_second_largest(numbers, expected):
    assert af.second_largest(numbers) == expected

# 8. Count Positive, Negative and Zero Values Tests
@pytest.mark.parametrize("numbers, expected", [
    ([5, -2, 0, 7, -9, 0], {"positive": 2, "negative": 2, "zero": 2}),
    ([], {"positive": 0, "negative": 0, "zero": 0})
])
def test_count_numbers(numbers, expected):
    assert af.count_numbers(numbers) == expected

# 9. List Average Without sum() Tests
@pytest.mark.parametrize("numbers, expected", [
    ([10, 20, 30, 40], 25.0),
    ([], "Invalid")
])
def test_average(numbers, expected):
    assert af.average(numbers) == expected

# 10. Search Element Manually Tests
@pytest.mark.parametrize("numbers, target, expected", [
    ([4, 8, 1, 8], 8, 1),
    ([4, 8, 1, 8], 10, -1)
])
def test_search_item(numbers, target, expected):
    assert af.search_item(numbers, target) == expected

# 11. Manual String Length Tests
@pytest.mark.parametrize("text, expected", [
    ("Python", 6),
    ("", 0)
])
def test_string_length(text, expected):
    assert af.string_length(text) == expected

# 12. Reverse a String Manually Tests
@pytest.mark.parametrize("text, expected", [
    ("function", "noitcnuf"),
    ("a", "a")
])
def test_reverse_text(text, expected):
    assert af.reverse_text(text) == expected

# 13. Check Palindrome String Tests
@pytest.mark.parametrize("text, expected", [
    ("Never odd or even", True),
    ("hello", False)
])
def test_is_text_palindrome(text, expected):
    assert af.is_text_palindrome(text) == expected

# 14. Print Right Triangle Pattern Tests
@pytest.mark.parametrize("n, expected", [
    (4, "*\n**\n***\n****"),
    (1, "*")
])
def test_print_triangle(n, expected):
    assert af.print_triangle(n) == expected

# 15. Find All Factors Tests
@pytest.mark.parametrize("n, expected", [
    (12, [1, 2, 3, 4, 6, 12]),
    (7, [1, 7])
])
def test_factors(n, expected):
    assert af.factors(n) == expected

# 16. Check Prime Using Function Tests
@pytest.mark.parametrize("n, expected", [
    (29, True),
    (4, False),
    (1, False)
])
def test_is_prime(n, expected):
    assert af.is_prime(n) == expected

# 17. Print Prime Numbers in a Range Tests
@pytest.mark.parametrize("start, end, expected", [
    (10, 20, [11, 13, 17, 19]),
    (8, 10, [])
])
def test_primes_between(start, end, expected):
    assert af.primes_between(start, end) == expected

# 18. Simple Calculator Function Tests
@pytest.mark.parametrize("a, b, operator, expected", [
    (20, 6, "%", 2),
    (5, 0, "/", "Error: Division by zero"),
    (5, 5, "?", "Error: Invalid operator")
])
def test_calculator(a, b, operator, expected):
    assert af.calculator(a, b, operator) == expected

# 19. Employee Salary Calculation Tests
@pytest.mark.parametrize("basic, expected", [
    (20000, 24700.0),
    (0, 0.0)
])
def test_net_salary(basic, expected):
    assert af.net_salary(basic) == expected

# 20. Shopping Cart Total Tests
@pytest.mark.parametrize("prices, quantities, expected", [
    ([1000, 500, 200], [3, 4, 5], 5400.0),
    ([100, 200], [2, 3], 800.0)
])
def test_cart_total(prices, quantities, expected):
    assert af.cart_total(prices, quantities) == expected

# --- Optional Challenge Tests ---
def test_marks_management_system_user_workflow():
    names = []
    marks = []
    
    # 1. Add Student Record: Vinod with marks 10.0
    assert af.add_student(names, marks, "Vinod", 10.0)
    
    # 2. Show All Student Records
    records = af.show_students(names, marks)
    assert "Vinod: 10.0" in records
    
    # 3. Find Student with Highest Marks
    highest_name, highest_mark = af.find_highest_marks(names, marks)
    assert highest_name == "Vinod"
    assert highest_mark == 10.0
    
    # 4. Search Student by Name: "vi" (Expected not found: -1 since it is only a partial match)
    assert af.search_student(names, marks, "vi") == -1
    
    # 5. Search Student by Name: "Vinod" (Expected found at index 0)
    assert af.search_student(names, marks, "Vinod") == 0
    
    # 6. Search Student by Name with different casing: "vinod" and "VINOD" (Expected found at index 0)
    assert af.search_student(names, marks, "vinod") == 0
    assert af.search_student(names, marks, "VINOD") == 0
