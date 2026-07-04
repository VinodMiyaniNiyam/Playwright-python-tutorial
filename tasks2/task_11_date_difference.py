# Task 11: Date Difference Calculator
# Topics: Datetime objects, functions

import datetime

def parse_date(date_str):
    try:
        return datetime.datetime.strptime(date_str.strip(), "%d-%m-%Y").date()
    except ValueError:
        return None

def date_difference(start_str, end_str):
    start = parse_date(start_str)
    end   = parse_date(end_str)

    if start is None:
        return None, "Invalid start date. Use DD-MM-YYYY format."
    if end is None:
        return None, "Invalid end date. Use DD-MM-YYYY format."
    if end < start:
        return None, "End date cannot be before start date."

    delta = end - start
    days  = delta.days
    weeks = days // 7

    return {"days": days, "weeks": weeks, "start": start, "end": end}, None

def print_date_report(result):
    print("=" * 40)
    print("    DATE DIFFERENCE REPORT")
    print("=" * 40)
    print(f"  Start Date   : {result['start'].strftime('%d-%m-%Y')}")
    print(f"  End Date     : {result['end'].strftime('%d-%m-%Y')}")
    print(f"  Difference   : {result['days']} days")
    print(f"  Complete Wks : {result['weeks']} weeks")
    print("=" * 40)

# Test Section
if __name__ == "__main__":
    # Test Case 1: Valid date range
    result, err = date_difference("01-01-2026", "04-07-2026")
    if err:
        print(f"Test Case 1 Error: {err}")
    else:
        print("Test Case 1: Valid range")
        print_date_report(result)
    print()

    # Test Case 2: Same dates
    result, err = date_difference("04-07-2026", "04-07-2026")
    if err:
        print(f"Test Case 2 Error: {err}")
    else:
        print("Test Case 2: Same dates")
        print_date_report(result)
    print()

    # Test Case 3: End before start
    result, err = date_difference("31-12-2026", "01-01-2026")
    print(f"Test Case 3: {err}")
