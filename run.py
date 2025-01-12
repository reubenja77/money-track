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
                print("\nInvalid choice. Please enter a number between 1 and 7.")
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
        return[]

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
            "amount": formatted_amount,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
        save_transactions(transactions)
        print(f"\n{transaction_type.capitalize()} of ${abs(float(formatted_amount)):.2f} added successfully!")
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
        print(f"{i}. {t_type}: Category: {transaction['category']} - ${abs(float(transaction['amount'])):.2f}")

def check_balance(transactions):
    """
    Calculate and display current balance.

    Args:
        transactions (list): Lists of transaction records.
    """
    balance = sum(float(transaction["amount"]) for transaction in transactions)
    print(f"Current Balance: ${balance:.2f}\n")

def view_transactions_by_category(transactions):
    category = input("Enter the category to filter by:\n").strip()
    filtered_transactions = [t for t in transactions if t["category"].lower() == category.lower()]
    if not filtered_transactions:
        print(f"No transactions found for category: {category}")
        return
    print(f"Transactions for category '{category}':\n")
    for i, transaction in enumerate(filtered_transactions, 1):
        t_type = transaction["type"].capitalize()
        print(f"{i}. {t_type}: {transaction['description']} - ${abs(transaction['amount']):.2f} - Date: {transaction['timestamp']}")

def generate_monthly_report(transactions):
    monthly_summary = {}
    for transaction in transactions:
        month = transaction["timestamp"][1:7] # Exact YYYY-MM
        if month not in monthly_summary:
            monthly_summary[month] = 0
        monthly_summary[month] += transaction["amount"]
    print("Monthly Report:\n")
    for month, total in sorted(monthly_summary.items()):
        print(f"{month}: ${total:.2f}")

def delete_transaction(transactions):
    view_transactions(transactions)
    try:
        choice = int(input("Enter the number of the transaction to delete:\n")) - 1
        if 0 <= choice < len(transactions):
            delete = transactions.pop(choice)
            save_transactions(transactions)
            print(f"Deleted transaction: {deleted['description']} - ${abs(delete['amount']):.2f}")
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