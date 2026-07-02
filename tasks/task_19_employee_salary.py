# Task 19: Employee Salary Calculation

def net_salary(basic):
    if basic < 0:
        return 0.0
        
    hra = 0.20 * basic
    da = 0.10 * basic
    gross = basic + hra + da
    tax = 0.05 * gross
    net = gross - tax
    
    return net

# Test Section
if __name__ == "__main__":
    # Test Case 1: Standard basic salary
    basic1 = 20000
    res1 = net_salary(basic1)
    print(f"Test Case 1: Basic = {basic1} -> Net Salary = {res1} (Expected: 24700.0)")
    
    # Test Case 2: Zero basic salary
    basic2 = 0
    res2 = net_salary(basic2)
    print(f"Test Case 2: Basic = {basic2} -> Net Salary = {res2} (Expected: 0.0)")
