# Money Tracker (Income and Expense Tracker)

import json
from datetime import datetime


def introduction():
    print("Welcome to The Money Tracker App!\n")
    print("The app that helps you keep track of your income and expenses.")
    print("\nLets get you started!/n")


def get_user_choice():
    """
    Display menu options and return user's choice.

    Returns an integer of User's menu choice.
    """
    print("Income and Expense Tracker Menu:\n")
    print("1. Add income or expense")
    print("2. View transactions")
    print("3. Check balance")
    print("4. View transactions by category")
    print("5. Generate monthly report")
    print("6. Delete a transaction")
    print("7. Exit")
    while True:
        try:
            choice = int(input("\nEnter your choice (1-7):\n"))
            if 1 <= choice <= 7:
                return choice
            else:
                print(
                    "\nInvalid choice. "
                    "Please enter a number between 1 and 7."
                )
        except ValueError:
            print("\nInvalid input. Please enter a valid number.")


def save_transactions(transactions, filename="transactions.json"):
    with open(filename, "w") as file:
        json.dump(transactions, file, indent=4)


def load_transactions(filename="transactions.json"):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def add_transaction(transactions):
    """
    Add an income or expense tranaction.

    Args:
        transactions (list): List of transaction records.
    """
    try:
        transaction_type = (
            input("\nEnter 'income' or 'expense':\n")
            .strip()
            .lower()
        )
        if transaction_type not in ["income", "expense"]:
            raise ValueError("Transaction type must be 'income' or 'expense'.")
        category = (
            input(
                "\nEnter the transaction category "
                "(e.g., 'Salary', 'Rent', 'Food'):\n"
            )
            .strip()
        )
        amount = float(input("\nEnter the amount:\n"))
        if amount <= 0:
            raise ValueError("Amount must be greater then 0.")

        # Negative value for expenses
        if transaction_type == "expense":
            amount = -amount

        # Format amount to 2 decimal places
        formatted_amount = "{:.2f}".format(amount)

        # Append the new transaction with all fields
        transactions.append({
            "type": transaction_type,
            "category": category,
            "amount": formatted_amount,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
        save_transactions(transactions)
        print(f"\n{transaction_type.capitalize()} of "
              f"${abs(float(formatted_amount)):.2f} added successfully!")
    except ValueError as e:
        print(f"Invalid input: {e}")


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
        print(f"{i}. {t_type}: Category: {transaction['category']} - "
              f"${abs(float(transaction['amount'])):.2f}")


def check_balance(transactions):
    """
    Calculate and display current balance.

    Args:
        transactions (list): Lists of transaction records.
    """
    balance = sum(float(transaction["amount"]) for transaction in transactions)
    print(f"Current Balance: ${balance:.2f}\n")


def view_transactions_by_category(transactions):
    """
    Display transactions filtered by a specific category.

    Args:
        transactions (list): List of transaction dictionaries.
    This functions prompts users to enter a category and then filters the
    provided transactions list to include only those transactions that
    match the specified category.
    If no matching transactions are found, an appropriate message is displayed.
    Otherwise, the filtered transactions are displayed with their details.
    """
    category = input("Enter the category to filter by:\n").strip()
    filtered_transactions = [
        t for t in transactions if t["category"].lower() == category.lower()
    ]
    if not filtered_transactions:
        print(f"No transactions found for category: {category}")
        return
    print(f"Transactions for category '{category}':\n")
    for i, transaction in enumerate(filtered_transactions, 1):
        t_type = transaction["type"].capitalize()
        amount = float(transaction["amount"])
        # Ensure amount is a float
        print(f"{i}. {t_type}: ${abs(amount):.2f} - "
              f"Date: {transaction['timestamp']}")


def generate_monthly_report(transactions):
    """
    Generates a monthly summary of income and expenses.

    Args:
        transactions list: List of transaction dictionaries.
    This function calculates and displays the total income and expenses
    for each month recorded in the transactions history.
    It iterates through the transactions, groups then by month
    (YYYY-MM), and calculates the sum of amounts for each month.
    Finally, it displays the monthly summary in a user-friendly format.
    """
    monthly_summary = {}
    for transaction in transactions:
        month = transaction["timestamp"][:7]
        # Extract YYYY-MM
        if month not in monthly_summary:
            monthly_summary[month] = 0
        monthly_summary[month] += float(transaction["amount"])
        # Convert to float
    print("Monthly Report:\n")
    for month, total in sorted(monthly_summary.items()):
        print(f"{month}: ${total:.2f}")


def delete_transaction(transactions):
    """
    Deletes a specified transaction from the list of transactions.

    Args:
        transactions (list): List of transaction dictionaries.
    This functions first displays the list of transactions to the user.
    Then, it prompts the user to enter the number of the transaction
    they wish to delete.
    If a valid transaction number is provided, the corresponding
    transaction is removed from the list.
    The function includes input validation and error handling
    to ensure a smooth and safe deletion process.
    """
    view_transactions(transactions)
    try:
        choice = int(input(
            "Enter the number of the transaction to delete:\n")) - 1
        if 0 <= choice < len(transactions):
            deleted = transactions.pop(choice)
            save_transactions(transactions)
            print(f"Deleted transaction: ${abs(float(deleted['amount'])):.2f}")
            # Ensure amount is a float
        else:
            print("Invalid choice")
    except ValueError:
        print("Invalid input. Please enter a valid number.")


def main():
    """
    Main function to run the income and expense tracker.
    Chains other functions to provide functionality.
    """
    transactions = load_transactions()
    while True:
        choice = get_user_choice()
        if choice == 1:
            add_transaction(transactions)
        elif choice == 2:
            view_transactions(transactions)
        elif choice == 3:
            check_balance(transactions)
        elif choice == 4:
            view_transactions_by_category(transactions)
        elif choice == 5:
            generate_monthly_report(transactions)
        elif choice == 6:
            delete_transaction(transactions)
        elif choice == 7:
            print("\nExiting the Income Money Tracker. Goodbye!")
            break


# Run program
if __name__ == "__main__":
    main()
