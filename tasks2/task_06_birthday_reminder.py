# Task 6: Birthday Reminder
# Topics: Date objects, dictionaries, loops

import datetime

birthdays = {
    "Alice":   datetime.date(1998, 7, 4),
    "Bob":     datetime.date(1995, 12, 25),
    "Charlie": datetime.date(2000, 1, 15),
    "Diana":   datetime.date(1997, 7, 4),
    "Eve":     datetime.date(2001, 3, 8),
}

def days_until_next_birthday(birthday, today):
    # Next birthday this year
    try:
        next_bday = datetime.date(today.year, birthday.month, birthday.day)
    except ValueError:
        # Feb 29 in non-leap year
        next_bday = datetime.date(today.year, birthday.month + 1, 1)

    if next_bday < today:
        # Birthday already passed this year, check next year
        try:
            next_bday = datetime.date(today.year + 1, birthday.month, birthday.day)
        except ValueError:
            next_bday = datetime.date(today.year + 1, birthday.month + 1, 1)

    delta = next_bday - today
    return delta.days

def check_birthdays(today=None):
    if today is None:
        today = datetime.date.today()

    print("=" * 45)
    print(f"  BIRTHDAY REMINDER  |  Today: {today}")
    print("=" * 45)

    today_birthdays = []
    for name, bday in birthdays.items():
        if bday.month == today.month and bday.day == today.day:
            today_birthdays.append(name)

    if today_birthdays:
        print("  ** TODAY'S BIRTHDAYS:")
        for name in today_birthdays:
            print(f"    -> Happy Birthday, {name}!")
    else:
        print("  No birthdays today.")

    print()
    print("  UPCOMING BIRTHDAYS:")
    for name, bday in birthdays.items():
        days_left = days_until_next_birthday(bday, today)
        if days_left == 0:
            print(f"    {name:<10} -> ** Today!")
        else:
            print(f"    {name:<10} -> {days_left} days left ({bday.strftime('%d %b')})")
    print("=" * 45)

# Test Section
if __name__ == "__main__":
    # Test Case 1: Using today's actual date
    print("Test Case 1: Using today's date")
    check_birthdays()
    print()

    # Test Case 2: Simulate a specific date matching Alice and Diana's birthday
    print("Test Case 2: Simulated date 04-Jul")
    check_birthdays(datetime.date(2026, 7, 4))
    print()

    # Test Case 3: Simulate Christmas day
    print("Test Case 3: Simulated date 25-Dec")
    check_birthdays(datetime.date(2026, 12, 25))
