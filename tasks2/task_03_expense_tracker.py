# Task 3: Simple Expense Tracker
# Topics: Dictionaries, loops, string functions

def add_expense(expenses, category, amount):
    category = category.strip().lower()
    valid_categories = ["food", "travel", "stationery", "other"]

    found = False
    for c in valid_categories:
        if c == category:
            found = True
            break

    if not found:
        return False, f"Invalid category '{category}'. Use: food, travel, stationery, other."

    if category in expenses:
        expenses[category] += amount
    else:
        expenses[category] = amount
    return True, "Expense added."

def view_summary(expenses):
    total = 0.0
    for amt in expenses.values():
        total += amt

    print("=" * 40)
    print("      EXPENSE SUMMARY")
    print("=" * 40)
    for cat, amt in expenses.items():
        pct = (amt / total * 100) if total > 0 else 0
        print(f"  {cat.title():<15} : Rs.{amt:<8.2f} ({pct:.1f}%)")
    print(f"  {'Total':<15} : Rs.{total:.2f}")
    print("=" * 40)
    return total

def highest_category(expenses):
    if not expenses:
        return None, 0
    top_cat = None
    top_amt = 0
    for cat, amt in expenses.items():
        if amt > top_amt:
            top_amt = amt
            top_cat = cat
    return top_cat, top_amt

# Test Section
if __name__ == "__main__":
    expenses = {}

    # Test Case 1: Add valid expenses
    add_expense(expenses, "Food", 500)
    add_expense(expenses, "TRAVEL", 300)
    add_expense(expenses, "stationery", 150)
    add_expense(expenses, "other", 200)
    add_expense(expenses, "food", 100)

    print("Test Case 1: View Summary")
    view_summary(expenses)
    print()

    # Test Case 2: Highest category
    cat, amt = highest_category(expenses)
    print(f"Test Case 2: Highest Category = {cat.title()} (Rs.{amt})")
    print()

    # Test Case 3: Invalid category
    ok, msg = add_expense(expenses, "entertainment", 100)
    print(f"Test Case 3: Add Invalid Category -> {msg}")
