# Money Tracker (Income and Expense Tracker)

import json
from datetime import datetime

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
            choice = int(input("\nEnter your choice (1-4):\n"))
            if 1 <= choice <= 4:
                return choice
            else:
                print("\nInvalid choice. Please enter a number between 1 and 4.")
        except ValueError:
            print("\nInvalid input. Please enter a valid number.")

def add_transaction(transactions):
    """
    Add an income or expense tranaction.

    Args:
        transactions (list): List of transaction records.
    """
    try:
        transaction_type = input("\nEnter 'income' or 'expense':\n").strip().lower()
        if transaction_type not in ["income", "expense"]:
            raise ValueError("Transaction type must be 'income' or 'expense'.")
        category = input("\nEnter the transaction category (e.g., 'Salary', 'Rent', 'Food'):\n").strip()
        amount = float(input("\nEnter the amount:\n"))
        if amount <= 0:
            raise ValueError("Amount must be greater then 0.")

        if transaction_type == "expense":
            amount = -amount # Negative value for expenses

        # Format amount to 2 decimal places
        formatted_amount = "{:.2f}".format(amount)

        # Append the new transaction with all fields
        transactions.append({
            "type": transaction_type, 
            "category": category, 
            "amount": formatted_amount
        })
        print(f"\n{transaction_type.capitalize()} of ${abs(float(formatted_amount)):.2f} added successfully!")
    except ValueError as e:
        print(f"Invalid input: {e}")
        print("Category")

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
        print(f"{i}. {t_type}: Category: {transaction['category']} - ${abs(float(transaction['amount'])):.2f}")

def check_balance(transactions):
    """
    Calculate and display current balance.

    Args:
        transactions (list): Lists of transaction records.
    """
    balance = sum(float(transaction["amount"]) for transaction in transactions)
    print(f"Current Balance: ${balance:.2f}\n")

def main():
    """
    Main function to run the income and expense tracker.
    Chains other functions to provide functionality.
    """
    transactions = []
    while True:
        choice = get_user_choice()
        if choice == 1:
            add_transaction(transactions)
        elif choice == 2:
            view_transactions(transactions)
        elif choice == 3:
            check_balance(transactions)
        elif choice == 4:
            print("\nExiting the Income Money Tracker. Goodbye!")
            break

# Run program
if __name__ == "__main__":
    main()