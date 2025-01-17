# Money Tracker App (Income and Expense Tracker)

import os
import json
from datetime import datetime
from colorama import Fore, Back, Style, init


#  Initialise colorama
init(autoreset=True)


def clear():
    """
    Clear function to clean-up the terminal so things don't get messy.
    """
    os.system("cls" if os.name == "nt" else "clear")


def introduction():
    print("Welcome to The Money Tracker App!\n")
    print(
        "The app that helps you manage your personal finances "
        "by tracking your income and expenses.\n"
    )
    print(Back.GREEN + Fore.WHITE + "Let's get you started!\n")


def get_user_choice():
    """
    Display menu options and return user's choice.

    Returns an integer of User's menu choice.
    """
    print("\nIncome and Expense Menu:\n")
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
                print(Back.RED + Fore.WHITE + (
                    "\nInvalid choice. "
                    "\nPlease enter a number "
                    "between 1 and 7." + Style.RESET_ALL
                ))
        except ValueError:
            print(Back.RED + Fore.WHITE + (
                "\nInvalid input. Please enter "
                "a valid number." + Style.RESET_ALL
            ))


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
    # Loop to stay in "Add transaction" menu
    while True:
        clear()  # Clear the screen before displaying the Add Transaction
        try:
            print("\n--- Add Transaction Menu ---")
            transaction_type = (
                input(
                    "\nEnter 'income' or 'expense' "
                    "(or type 'back' to return to the main menu):\n"
                )
                .strip()
                .lower()
            )
            if transaction_type == "back":
                print("Returning to the main menu...")
                break  # Exit the loop and return to the main menu
            if transaction_type not in ["income", "expense"]:
                print(
                    "Invalid input. Please enter 'income', 'expense', "
                    "or go 'back'."
                )
                continue

            category = (
                input(
                    "\nEnter the transaction category "
                    "(e.g., 'Salary', 'Rent', 'Food'):\n"
                )
                .strip()
            )
            amount = float(input("\nEnter the amount:\n"))
            if amount <= 0:
                print("Amount must be greater than 0.")
                continue

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

            # Print success message in colors with details and pause
            print(
                Back.GREEN + Fore.WHITE +
                f"\n{transaction_type.capitalize()} of "
                f"${abs(float(formatted_amount)):.2f} "
                f"added successfully to category! "
                f"'{category}'." +
                Style.RESET_ALL
            )
            input("\nPress Enter to continue...")
            clear()  # Clear the screen after exiting the Add Transaction

        except ValueError:
            print("Invalid input. Please enter valid details.")


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
    balance = sum(
        float(transaction["amount"])
        for transaction in transactions
    )
    print(Back.GREEN + Fore.WHITE + (
        "\nCurrent Balance:" +
        Style.RESET_ALL
    ))
    print(f"${balance:.2f}\n" + Style.RESET_ALL)


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
    if not transactions:
        print(Back.BLUE + Fore.WHITE + "No transactions recorded yet!")
        return

    # Display all recorded transactions for context
    print("\n--- All Recorded Transactions ---\n")
    for i, transaction in enumerate(transactions, 1):
        t_type = transaction["type"].capitalize()
        print(f"{i}. {t_type}: {transaction['category']} - "
              f"${abs(float(transaction['amount'])):.2f} - "
              f"Date: {transaction['timestamp']}")

    # Filter transactions by category
    category = input("\nEnter the category to filter by:\n").strip()
    filtered_transactions = [
        t for t in transactions if t["category"].lower() == category.lower()
    ]

    if not filtered_transactions:
        print(f"\nNo transactions found for category: {category}")
        return

    print(f"\n--- Transactions for Category '{category}' ---\n")
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
    print(Back.GREEN + Fore.WHITE + "\nMonthly Report:")
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
    if not transactions:
        print(Back.RED + Fore.WHITE + (
            "No transactions recorded yet to be deleted."
            + Style.RESET_ALL
        ))
        return

    while True:
        view_transactions(transactions)
        try:
            choices = input(
                "\nEnter the number of the transaction to delete "
                "(seperate multiple numbers with commas):\n"
            ).strip()

            # Check for empty input or non-numeric values
            if not choices:
                print(Back.RED + Fore.WHITE + (
                    "Please enter a number."
                    + Style.RESET_ALL
                ))
                continue

            # Parse input and validate
            indices = [
                int(choice.strip()) - 1
                for choice in choices.split(",")
                if choice.strip().isdigit()
            ]

            # Check if any valid indices exist
            if not indices:
                print(Back.RED + Fore.WHITE + (
                    "\nPlease enter a valid number "
                    "from the recorded transactions "
                    "you wish to delete "
                    "(seperate multiple numbers with commas)." +
                    Style.RESET_ALL
                ))
                continue

            invalid_indices = [
                i for i in indices
                if 1 < 0 or i >= len(transactions)
            ]
            if invalid_indices:
                print(Back.RED + Fore.WHITE + (
                    f"\nInvalid transaction number(s): "
                    f"\nPlease enter a valid number "
                    f"from the recorded transactions "
                    f"you wish to delete "
                    f"(seperate multiple numbers with commas)."
                    f"\n{', '.join(str(i + 1) for i in invalid_indices)}." +
                    Style.RESET_ALL
                ))
                continue

            # Confirm deletion
            print(Back.BLUE + Fore.WHITE + (
                "\nThe following will be deleted" +
                Style.RESET_ALL
            ))
            for i in sorted(indices):
                transaction = transactions[i]
                print(f"- {transaction['type'].capitalize()} | "
                      f"Category: {transaction['category']} | "
                      f"Amount: ${abs(float(transaction['amount'])):.2f} | "
                      f"Date: {transaction['timestamp']}")

            confirm = (
                input(
                    "\nAre you sure you want to delete "
                    "these transactions? (yes/no):\n"
                )
                .strip()
                .lower()
            )
            if confirm != "yes":
                print(Back.BLUE + Fore.WHITE + (
                    "\nNo transactions were deleted." +
                    Style.RESET_ALL
                ))
                return

            # Delete transactions in reverse order to avoid index shifting
            for i in sorted(indices, reverse=True):
                transactions.pop(i)

            save_transactions(transactions)
            print(Back.GREEN + Fore.WHITE + (
                "Selected transactions deleted successfully."
            ))
            return

        except ValueError:
            print(Back.RED + Fore.WHITE + "Invalid input.")
            print(Back.RED + Fore.WHITE + (
                "\nPlease enter a valid numbers seperated by commas." +
                Style.RESET_ALL
            ))


def main():
    """
    Main function to run the income and expense tracker.
    Chains other functions to provide functionality.
    """
    introduction()
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
            print("\nExiting The Money Tracker.\nGoodbye!\n")
            break


# Run program
if __name__ == "__main__":
    main()
