# Task 3: Simple ATM Withdrawal

def atm_withdraw(balance, amount):
    # Validation checks
    if amount <= 0:
        return "Amount must be positive"
    if amount % 100 != 0:
        return "Amount must be a multiple of 100"
    if amount > balance:
        return "Insufficient balance"
    
    # Return updated balance
    return balance - amount

# Test Section
if __name__ == "__main__":
    # Test Case 1: Valid withdrawal
    bal1, amt1 = 5000, 1200
    res1 = atm_withdraw(bal1, amt1)
    print(f"Test Case 1: Balance={bal1}, Withdraw={amt1} -> New Balance = {res1} (Expected: 3800)")
    
    # Test Case 2: Invalid multiple of 100
    bal2, amt2 = 5000, 1250
    res2 = atm_withdraw(bal2, amt2)
    print(f"Test Case 2: Balance={bal2}, Withdraw={amt2} -> Result = {res2} (Expected: Amount must be a multiple of 100)")
    
    # Test Case 3: Insufficient balance
    bal3, amt3 = 1000, 1500
    res3 = atm_withdraw(bal3, amt3)
    print(f"Test Case 3: Balance={bal3}, Withdraw={amt3} -> Result = {res3} (Expected: Insufficient balance)")
