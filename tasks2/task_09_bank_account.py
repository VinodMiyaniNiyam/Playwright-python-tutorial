# Task 9: Bank Account Mini System
# Topics: Functions, branching, loops

import datetime

def create_account(name, opening_balance):
    return {
        "name": name,
        "balance": opening_balance,
        "transactions": []
    }

def deposit(account, amount):
    if amount <= 0:
        return False, "Deposit amount must be greater than 0."
    account["balance"] += amount
    account["transactions"].append({
        "date": str(datetime.date.today()),
        "type": "Deposit",
        "amount": amount,
        "balance": account["balance"]
    })
    return True, f"Rs.{amount} deposited. New balance: Rs.{account['balance']}"

def withdraw(account, amount):
    if amount <= 0:
        return False, "Withdrawal amount must be greater than 0."
    if amount > account["balance"]:
        return False, f"Insufficient balance. Available: Rs.{account['balance']}"
    account["balance"] -= amount
    account["transactions"].append({
        "date": str(datetime.date.today()),
        "type": "Withdraw",
        "amount": amount,
        "balance": account["balance"]
    })
    return True, f"Rs.{amount} withdrawn. New balance: Rs.{account['balance']}"

def display_balance(account):
    print(f"  Account Holder : {account['name']}")
    print(f"  Balance        : Rs.{account['balance']}")

def print_transaction_history(account):
    print("=" * 55)
    print("    TRANSACTION HISTORY")
    print("=" * 55)
    print(f"  {'Date':<12} {'Type':<12} {'Amount':<12} {'Balance'}")
    print("-" * 55)
    for t in account["transactions"]:
        print(f"  {t['date']:<12} {t['type']:<12} Rs.{t['amount']:<10} Rs.{t['balance']}")
    print("=" * 55)

# Test Section
if __name__ == "__main__":
    # Test Case 1: Normal deposits and withdrawals
    acc = create_account("Vinod", 5000)
    print("Test Case 1: Deposits and Withdrawals")
    print(deposit(acc, 2000)[1])
    print(withdraw(acc, 1500)[1])
    print(deposit(acc, 500)[1])
    display_balance(acc)
    print()
    print_transaction_history(acc)
    print()

    # Test Case 2: Insufficient balance
    ok, msg = withdraw(acc, 50000)
    print(f"Test Case 2: {msg}")
    print()

    # Test Case 3: Invalid amount
    ok, msg = deposit(acc, -100)
    print(f"Test Case 3: {msg}")
