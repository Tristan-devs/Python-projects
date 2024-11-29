def welcome_message():
    print("Welcome to the Daily Expense Tracker!")

def log_expense(expenses):
    try:
        amount = float(input("Enter the expense amount: "))
        category = input("Enter the expense category (e.g., Food, Transport, Entertainment): ")
        description = input("Enter a description of the expense: ")
        expenses.append({'amount': amount, 'category': category, 'description': description})
        print("Expense logged successfully!")
    except ValueError:
        print("Invalid input. Please enter a valid number for the amount.")

def view_summary(expenses):
    if not expenses:
        print("No expenses logged yet.")
        return

    total_amount = sum(expense['amount'] for expense in expenses)
    print(f"\nTotal Expenses: {total_amount}")
    
    category_summary = {}
    for expense in expenses:
        category = expense['category']
        if category in category_summary:
            category_summary[category] += expense['amount']
        else:
            category_summary[category] = expense['amount']
    
    print("\nExpenses by Category:")
    for category, amount in category_summary.items():
        print(f"{category}: {amount}")

def main():
    expenses = []
    welcome_message()

    while True:
        print("\nMenu:")
        print("1. Log an Expense")
        print("2. View Expense Summary")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            log_expense(expenses)
        elif choice == '2':
            view_summary(expenses)
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")

if __name__ == "__main__":
    main()


