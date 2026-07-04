# Task 2: Attendance Eligibility Checker
# Topics: Date objects, branching, functions

import datetime

def calculate_attendance(total_days, attended_days):
    if total_days <= 0:
        return 0.0
    return (attended_days / total_days) * 100

def check_eligibility(total_days, attended_days, medical_days=0):
    attendance_pct = calculate_attendance(total_days, attended_days)

    if attendance_pct < 75:
        # Recalculate with medical leave
        effective_total = total_days - medical_days
        effective_attended = attended_days
        attendance_pct = calculate_attendance(effective_total, effective_attended)

    return round(attendance_pct, 2)

def print_eligibility_report(name, total_days, attended_days, medical_days=0):
    today = datetime.date.today()
    final_pct = check_eligibility(total_days, attended_days, medical_days)

    print("=" * 45)
    print("    ATTENDANCE ELIGIBILITY REPORT")
    print("=" * 45)
    print(f"  Student       : {name}")
    print(f"  Report Date   : {today}")
    print(f"  Total Days    : {total_days}")
    print(f"  Attended Days : {attended_days}")
    print(f"  Medical Days  : {medical_days}")
    print(f"  Attendance    : {final_pct}%")
    if final_pct >= 75:
        print(f"  Status        : ELIGIBLE for Exam")
    else:
        print(f"  Status        : NOT ELIGIBLE (Below 75%)")
    print("=" * 45)

# Test Section
if __name__ == "__main__":
    # Test Case 1: Eligible without medical leave
    print_eligibility_report("Alice", 100, 80)
    print()

    # Test Case 2: Not eligible - below 75%
    print_eligibility_report("Bob", 100, 60)
    print()

    # Test Case 3: Eligible after medical leave adjustment
    print_eligibility_report("Charlie", 100, 68, medical_days=10)
