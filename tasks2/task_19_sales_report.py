# Task 19: Monthly Sales Report
# Topics: Dictionaries, loops, functions

def calculate_total(sales):
    total = 0.0
    for amt in sales.values():
        total += amt
    return round(total, 2)

def calculate_average(sales):
    total = calculate_total(sales)
    count = len(sales)
    if count == 0:
        return 0.0
    return round(total / count, 2)

def highest_sales_day(sales):
    top_day = None
    top_amt = 0.0
    for day, amt in sales.items():
        if amt > top_amt:
            top_amt = amt
            top_day = day
    return top_day, top_amt

def lowest_sales_day(sales):
    low_day = None
    low_amt = None
    for day, amt in sales.items():
        if low_amt is None or amt < low_amt:
            low_amt = amt
            low_day = day
    return low_day, low_amt

def print_sales_report(sales, month_name="Month"):
    total   = calculate_total(sales)
    avg     = calculate_average(sales)
    hi_day, hi_amt = highest_sales_day(sales)
    lo_day, lo_amt = lowest_sales_day(sales)

    print("=" * 50)
    print(f"    MONTHLY SALES REPORT - {month_name.upper()}")
    print("=" * 50)
    print(f"  {'Day':<10} {'Sales Amount':>15}")
    print("-" * 50)
    for day, amt in sales.items():
        print(f"  Day {day:<6} Rs.{amt:>12.2f}")
    print("-" * 50)
    print(f"  Total Sales    : Rs.{total:.2f}")
    print(f"  Average/Day    : Rs.{avg:.2f}")
    print(f"  Highest Day    : Day {hi_day} (Rs.{hi_amt:.2f})")
    print(f"  Lowest Day     : Day {lo_day} (Rs.{lo_amt:.2f})")
    print("=" * 50)

# Test Section
if __name__ == "__main__":
    # Test Case 1: 10-day sales data
    sales1 = {1:1200, 2:850, 3:2300, 4:990, 5:1750, 6:3100, 7:650, 8:1400, 9:2200, 10:1800}
    print("Test Case 1: 10-Day Sales Report")
    print_sales_report(sales1, "July")
    print()

    # Test Case 2: Flat sales (all same)
    sales2 = {day: 1000.0 for day in range(1, 6)}
    print("Test Case 2: Uniform Sales")
    print_sales_report(sales2, "Test Month")
    print()

    # Test Case 3: Single day
    sales3 = {1: 5000.0}
    print("Test Case 3: Single Day")
    print_sales_report(sales3, "Single Day")
