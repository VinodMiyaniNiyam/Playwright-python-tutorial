# Task 2: Electricity Bill Calculator

def electricity_bill(units):
    if units < 0:
        return 0.0
    
    # Calculate bill using slabs:
    # First 100 units at 5 per unit
    # Next 100 units at 7 per unit
    # Remaining units at 10 per unit
    if units <= 100:
        bill = units * 5.0
    elif units <= 200:
        bill = (100 * 5.0) + ((units - 100) * 7.0)
    else:
        bill = (100 * 5.0) + (100 * 7.0) + ((units - 200) * 10.0)
        
    return bill

# Test Section
if __name__ == "__main__":
    # Test Case 1: Within first slab
    units1 = 80
    result1 = electricity_bill(units1)
    print(f"Test Case 1: Units = {units1} -> Bill = {result1} (Expected: 400.0)")
    
    # Test Case 2: Crossing into second slab
    units2 = 150
    result2 = electricity_bill(units2)
    print(f"Test Case 2: Units = {units2} -> Bill = {result2} (Expected: 850.0)")
    
    # Test Case 3: Crossing into third slab
    units3 = 250
    result3 = electricity_bill(units3)
    print(f"Test Case 3: Units = {units3} -> Bill = {result3} (Expected: 1700.0)")
