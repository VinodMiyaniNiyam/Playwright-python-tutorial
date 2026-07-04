# Task 5: Password Strength Validator
# Topics: String functions, branching, functions

def check_password_strength(password):
    length = len(password)
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    special_chars = "!@#$%^&*()-_=+[]{}|;:',.<>?/\\`~\""
    suggestions = []

    if length < 8:
        suggestions.append("Use at least 8 characters")

    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char in special_chars:
            has_special = True

    if not has_upper:
        suggestions.append("Add at least one uppercase letter")
    if not has_lower:
        suggestions.append("Add at least one lowercase letter")
    if not has_digit:
        suggestions.append("Add at least one digit (0-9)")
    if not has_special:
        suggestions.append("Add at least one special character (!@#$...)")

    score = 0
    if length >= 8:
        score += 1
    if has_upper:
        score += 1
    if has_lower:
        score += 1
    if has_digit:
        score += 1
    if has_special:
        score += 1

    if score == 5:
        strength = "Strong"
    elif score >= 3:
        strength = "Medium"
    else:
        strength = "Weak"

    return strength, suggestions

def print_password_report(password):
    strength, suggestions = check_password_strength(password)
    print(f"  Password : {password}")
    print(f"  Strength : {strength}")
    if suggestions:
        print("  Suggestions:")
        for s in suggestions:
            print(f"    - {s}")
    else:
        print("  Great! Your password is strong.")

# Test Section
if __name__ == "__main__":
    print("Test Case 1: Strong password")
    print_password_report("Secure@Pass1")
    print()

    print("Test Case 2: Medium password")
    print_password_report("password1A")
    print()

    print("Test Case 3: Weak password")
    print_password_report("abc")
