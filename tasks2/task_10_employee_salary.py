# Task 10: Employee Salary Calculator
# Topics: Functions, branching, dictionaries

def calculate_salary(name, basic, department):
    department = department.strip().upper()

    # HRA and DA rules per department
    if department == "IT":
        hra_pct = 0.30
        da_pct  = 0.20
    elif department == "HR":
        hra_pct = 0.25
        da_pct  = 0.15
    elif department == "SALES":
        hra_pct = 0.20
        da_pct  = 0.10
    else:
        hra_pct = 0.15
        da_pct  = 0.08

    hra   = basic * hra_pct
    da    = basic * da_pct
    gross = basic + hra + da
    pf    = basic * 0.12
    net   = gross - pf

    return {
        "name":       name,
        "department": department,
        "basic":      basic,
        "hra":        round(hra, 2),
        "da":         round(da, 2),
        "gross":      round(gross, 2),
        "pf":         round(pf, 2),
        "net_salary": round(net, 2)
    }

def print_salary_slip(slip):
    print("=" * 45)
    print("         SALARY SLIP")
    print("=" * 45)
    print(f"  Name         : {slip['name']}")
    print(f"  Department   : {slip['department']}")
    print("-" * 45)
    print(f"  Basic Salary : Rs.{slip['basic']:.2f}")
    print(f"  HRA          : Rs.{slip['hra']:.2f}")
    print(f"  DA           : Rs.{slip['da']:.2f}")
    print(f"  Gross Salary : Rs.{slip['gross']:.2f}")
    print(f"  PF (12%)     : Rs.{slip['pf']:.2f}")
    print("-" * 45)
    print(f"  NET SALARY   : Rs.{slip['net_salary']:.2f}")
    print("=" * 45)

# Test Section
if __name__ == "__main__":
    # Test Case 1: IT department
    slip1 = calculate_salary("Vinod", 30000, "IT")
    print("Test Case 1: IT Department")
    print_salary_slip(slip1)
    print()

    # Test Case 2: HR department
    slip2 = calculate_salary("Priya", 25000, "HR")
    print("Test Case 2: HR Department")
    print_salary_slip(slip2)
    print()

    # Test Case 3: Other department
    slip3 = calculate_salary("Amit", 20000, "Finance")
    print("Test Case 3: Other Department")
    print_salary_slip(slip3)
