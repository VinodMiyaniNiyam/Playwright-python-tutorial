# Task 4: Library Book Search System
# Topics: Dictionaries, loops, string functions

library = {
    "B001": {"title": "Python Programming", "author": "Guido Rossum", "status": "Available"},
    "B002": {"title": "Data Structures", "author": "Thomas Cormen", "status": "Issued"},
    "B003": {"title": "Web Development", "author": "Jon Duckett", "status": "Available"},
    "B004": {"title": "Machine Learning", "author": "Andrew Ng", "status": "Issued"},
    "B005": {"title": "Database Systems", "author": "Ramez Elmasri", "status": "Available"},
    "B006": {"title": "Operating Systems", "author": "Abraham Silberschatz", "status": "Available"},
    "B007": {"title": "Computer Networks", "author": "Andrew Tanenbaum", "status": "Issued"},
    "B008": {"title": "Software Engineering", "author": "Ian Sommerville", "status": "Available"},
    "B009": {"title": "Artificial Intelligence", "author": "Stuart Russell", "status": "Available"},
    "B010": {"title": "Cloud Computing", "author": "Rajkumar Buyya", "status": "Issued"},
}

def search_by_title(keyword):
    keyword = keyword.strip().lower()
    results = []
    for code, info in library.items():
        if keyword in info["title"].lower():
            results.append((code, info))
    return results

def check_status(book_code):
    book_code = book_code.strip().upper()
    if book_code in library:
        return library[book_code]["status"]
    return "Book not found"

def issue_book(book_code):
    book_code = book_code.strip().upper()
    if book_code not in library:
        return "Book not found"
    if library[book_code]["status"] == "Issued":
        return "Book is already issued"
    library[book_code]["status"] = "Issued"
    return f"Book '{library[book_code]['title']}' issued successfully"

def return_book(book_code):
    book_code = book_code.strip().upper()
    if book_code not in library:
        return "Book not found"
    if library[book_code]["status"] == "Available":
        return "Book is already available"
    library[book_code]["status"] = "Available"
    return f"Book '{library[book_code]['title']}' returned successfully"

# Test Section
if __name__ == "__main__":
    # Test Case 1: Search by keyword
    print("Test Case 1: Search 'python'")
    results = search_by_title("python")
    for code, info in results:
        print(f"  [{code}] {info['title']} by {info['author']} - {info['status']}")
    print()

    # Test Case 2: Check status
    print("Test Case 2: Check status of B002")
    print(f"  Status: {check_status('B002')}")
    print()

    # Test Case 3: Issue and return book
    print("Test Case 3: Issue book B001")
    print(f"  {issue_book('B001')}")
    print(f"  Status now: {check_status('B001')}")
    print(f"  {return_book('B001')}")
    print(f"  Status now: {check_status('B001')}")
