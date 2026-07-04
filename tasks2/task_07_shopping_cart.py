# Task 7: Shopping Cart Billing System
# Topics: Functions, dictionaries, branching, loops

shop_items = {
    "apple":    25.0,
    "bread":    40.0,
    "milk":     60.0,
    "butter":   80.0,
    "rice":     55.0,
    "sugar":    45.0,
    "biscuits": 30.0,
    "coffee":   120.0,
}

def add_to_cart(cart, item_name, quantity):
    item_name = item_name.strip().lower()
    if item_name not in shop_items:
        return False, f"Item '{item_name}' not found in shop."
    if quantity <= 0:
        return False, "Quantity must be greater than 0."
    if item_name in cart:
        cart[item_name] += quantity
    else:
        cart[item_name] = quantity
    return True, f"Added {quantity} x {item_name.title()} to cart."

def calculate_bill(cart):
    subtotal = 0.0
    for item, qty in cart.items():
        subtotal += shop_items[item] * qty

    discount = 0.0
    if subtotal > 1000:
        discount = subtotal * 0.10

    after_discount = subtotal - discount
    tax = after_discount * 0.05
    final = after_discount + tax

    return round(subtotal, 2), round(discount, 2), round(tax, 2), round(final, 2)

def print_bill(cart):
    subtotal, discount, tax, final = calculate_bill(cart)
    print("=" * 45)
    print("         SHOPPING BILL")
    print("=" * 45)
    for item, qty in cart.items():
        price = shop_items[item]
        print(f"  {item.title():<15} {qty:>3} x Rs.{price:<8.2f} = Rs.{qty*price:.2f}")
    print("-" * 45)
    print(f"  {'Subtotal':<30} Rs.{subtotal:.2f}")
    if discount > 0:
        print(f"  {'Discount (10%)':<30} Rs.{discount:.2f}")
    print(f"  {'Tax (5%)':<30} Rs.{tax:.2f}")
    print(f"  {'TOTAL':<30} Rs.{final:.2f}")
    print("=" * 45)

# Test Section
if __name__ == "__main__":
    cart = {}

    # Test Case 1: Normal cart below 1000 (no discount)
    add_to_cart(cart, "Apple", 4)
    add_to_cart(cart, "Milk", 2)
    add_to_cart(cart, "Bread", 3)
    print("Test Case 1: Cart below Rs.1000")
    print_bill(cart)
    print()

    # Test Case 2: Cart above 1000 (10% discount applies)
    cart2 = {}
    add_to_cart(cart2, "Coffee", 10)
    add_to_cart(cart2, "Butter", 5)
    add_to_cart(cart2, "Rice", 6)
    print("Test Case 2: Cart above Rs.1000 (Discount Applies)")
    print_bill(cart2)
    print()

    # Test Case 3: Invalid item
    ok, msg = add_to_cart(cart2, "Pizza", 2)
    print(f"Test Case 3: {msg}")
