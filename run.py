def get_user_choice():
    """
    Display menu options and return user's choice.

    Returns an integer of User's menu choice.
    """
    print("Income and Expense Tracker Menu:\n")
    print("1. Add income or expense")
    print("2. View transactions")
    print("3. Check balance")
    print("4. Exit")
    while True:
        try:
            choice = int(input("Enter your choice (1-4): "))
            if 1 <= choice <= 4:
                return choice
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

"""
# Test cases
def test_get_user_choice():
    # Test valid input
    assert get_user_choice() == 1  # Assuming User enters "1"
    assert get_user_choice() == 2  # Assuming user enters "2"
    assert get_user_choice() == 3  # Assuming User enters "3"
    assert get_user_choice() == 4  # Assuming User enters "4"

    # Test invalid input (out of range)
    try:
        get_user_choice() # Assuming user enters "5"
        assert False, "Expected ValueError for invalid input"
    except ValueError:
        pass

    # Test invalid input (non-numeric)
    try:
        get_user_choice() # Assuming user enters "a"
        assert False, "Expected ValueError for non-numeric input"
    except ValueError:
        pass

if __name__ == "__main__":
    test_get_user_choice()
    print("All tests passed!")
"""

def add_transaction(transactions):
    """
    Add an income or expense tranaction.

    Args:
        transactions (list): List of transaction records.
    """
    try:
        transaction_type = input("Enter 'income' or 'expense':\n").strip().lower()
        if transaction_type not in ["income", "expense"]:
            raise ValueError("Transaction. type must be 'income' or 'expense'.")
        description = input("Enter the transaction description:\n").strip()
        amount = float(input("Enter the amount:\n"))
        if amount <= 0:
            raise ValueError("Amount must be greater then 0.")

        if transaction_type == "expense":
            amount = -amount # Negative value for expenses

        # Format amount to 2 decimal places
        formatted_amount = "{:.2f}".format(amount)

        transactions.append({"type": transaction_type, "description": description, "amount": formatted_amount})
        print(f"{transaction_type.capitalize()} of ${abs(float(formatted_amount)):.2f} added successfully!")
    except ValueError as e:
        print(f"Invalid input: {e}")


# Test case for adding transaction
def test_add_transaction_interactive():
    transactions = []

    print("**Testing valid income transaction**")
    add_transaction(transactions)

    print("**Testing valid expense transaction**")
    add_transaction(transactions)

    print("**Testing invalid transaction type**")
    try:
        add_transaction(transactions)
    except ValueError:
        print("ValueError raised as expected.")

    print("**Testing invalid amount (zero)**")
    try:
        add_transaction(transactions)
    except ValueError:
        print("ValueError raised as expected.")

    print("**Testing invalid amount (negative)**")
    try:
        add_transaction(transactions)
    except ValueError:
        print("ValueError raised as expected.")

if __name__ == "__main__":
    test_add_transaction_interactive()


def view_transactions(transactions):
    """
    Display all recorded transactions

    Args:
        transactions (list): List of transaction records.
    """
    if not transactions:
        print("No transactions recorded yet.")
        return
    print("Recorded Transactions:\n")
    for i, transaction in enumerate(transactions, 1):
        t_type = transaction["type"].capitalize()
        print(f"{i}. {t_type}: {transaction['description']} - ${abs(float(transaction['formatted_amount'])):.2f}")

# Test case for view transaction
def test_view_transactions_interactive():
    transactions = []

    # Test empty transactions list
    print("**Testing empty transactions list:\n**")
    view_transactions(transactions)

    # Add sample transaction
    transactions.append({
        "type": "income",
        "description": "Salary",
        "formatted_amount": "1000.50"
    })
    transactions.append({
        "type": "expense",
        "description": "Groceries",
        "formatted_amount": "-50.25"
    })

    print("**Testing transactions with data\n**")
    view_transactions(transactions)

if __name__ == "__main__":
    test_view_transactions_interactive()