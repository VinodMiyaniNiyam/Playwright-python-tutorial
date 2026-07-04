# Task 12: Contact Book
# Topics: Dictionaries, loops, string functions

contacts = {}

def validate_mobile(mobile):
    if len(mobile) != 10:
        return False
    for ch in mobile:
        if not ch.isdigit():
            return False
    return True

def add_contact(name, mobile, email):
    if not validate_mobile(mobile):
        return False, "Mobile must be exactly 10 digits."
    key = name.strip().lower()
    contacts[key] = {"name": name.strip(), "mobile": mobile, "email": email.strip()}
    return True, f"Contact '{name}' added."

def search_contact(name):
    key = name.strip().lower()
    if key in contacts:
        return contacts[key]
    return None

def update_contact(name, mobile=None, email=None):
    key = name.strip().lower()
    if key not in contacts:
        return False, "Contact not found."
    if mobile:
        if not validate_mobile(mobile):
            return False, "Mobile must be exactly 10 digits."
        contacts[key]["mobile"] = mobile
    if email:
        contacts[key]["email"] = email
    return True, f"Contact '{name}' updated."

def delete_contact(name):
    key = name.strip().lower()
    if key in contacts:
        del contacts[key]
        return True, f"Contact '{name}' deleted."
    return False, "Contact not found."

def view_all():
    if not contacts:
        print("  No contacts found.")
        return
    print("=" * 50)
    print("    ALL CONTACTS")
    print("=" * 50)
    for key, info in contacts.items():
        print(f"  Name   : {info['name']}")
        print(f"  Mobile : {info['mobile']}")
        print(f"  Email  : {info['email']}")
        print("-" * 50)

# Test Section
if __name__ == "__main__":
    # Test Case 1: Add and view contacts
    print("Test Case 1: Add Contacts")
    print(add_contact("Vinod Miyani",   "9876543210", "vinod@email.com")[1])
    print(add_contact("Priya Sharma",   "8765432109", "priya@email.com")[1])
    print(add_contact("Rahul Gupta",    "7654321098", "rahul@email.com")[1])
    view_all()
    print()

    # Test Case 2: Search (case-insensitive)
    print("Test Case 2: Search 'priya sharma'")
    result = search_contact("priya sharma")
    if result:
        print(f"  Found: {result}")
    else:
        print("  Not found.")
    print()

    # Test Case 3: Invalid mobile
    ok, msg = add_contact("Bad Contact", "12345", "bad@email.com")
    print(f"Test Case 3: {msg}")
