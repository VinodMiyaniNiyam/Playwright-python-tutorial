# Task 16: Inventory Stock Alert
# Topics: Dictionaries, branching, loops

inventory = {
    "Pen":       {"quantity": 50,  "reorder_level": 20},
    "Notebook":  {"quantity": 10,  "reorder_level": 15},
    "Eraser":    {"quantity": 5,   "reorder_level": 10},
    "Ruler":     {"quantity": 30,  "reorder_level": 10},
    "Stapler":   {"quantity": 3,   "reorder_level": 5},
    "Marker":    {"quantity": 8,   "reorder_level": 12},
    "Tape":      {"quantity": 20,  "reorder_level": 8},
    "Scissors":  {"quantity": 2,   "reorder_level": 5},
}

def get_low_stock_items(inv):
    low = {}
    for item, data in inv.items():
        if data["quantity"] < data["reorder_level"]:
            low[item] = data
    return low

def update_stock(item_name, qty_change, operation="sale"):
    item_name = item_name.strip().title()
    if item_name not in inventory:
        return False, f"Item '{item_name}' not found."
    if operation == "sale":
        if qty_change > inventory[item_name]["quantity"]:
            return False, f"Cannot sell {qty_change}. Only {inventory[item_name]['quantity']} available."
        inventory[item_name]["quantity"] -= qty_change
    elif operation == "purchase":
        inventory[item_name]["quantity"] += qty_change
    return True, f"Stock updated. New quantity: {inventory[item_name]['quantity']}"

def print_stock_report():
    print("=" * 55)
    print("    INVENTORY STOCK REPORT")
    print("=" * 55)
    print(f"  {'Item':<15} {'Qty':>6} {'Reorder':>8} {'Status'}")
    print("-" * 55)
    for item, data in inventory.items():
        status = "LOW STOCK !" if data["quantity"] < data["reorder_level"] else "OK"
        print(f"  {item:<15} {data['quantity']:>6} {data['reorder_level']:>8}   {status}")
    print("=" * 55)

# Test Section
if __name__ == "__main__":
    # Test Case 1: Print stock report with alerts
    print("Test Case 1: Stock Report")
    print_stock_report()
    print()

    # Test Case 2: Show low stock items
    print("Test Case 2: Low Stock Items")
    low = get_low_stock_items(inventory)
    for item, data in low.items():
        print(f"  {item}: Only {data['quantity']} left (Reorder at {data['reorder_level']})")
    print()

    # Test Case 3: Update stock
    print("Test Case 3: Update Stock")
    ok, msg = update_stock("Pen", 5, "sale")
    print(f"  Sale 5 Pens    : {msg}")
    ok, msg = update_stock("Eraser", 50, "purchase")
    print(f"  Purchase 50 Erasers: {msg}")
    ok, msg = update_stock("Stapler", 100, "sale")
    print(f"  Sale 100 Staplers: {msg}")
