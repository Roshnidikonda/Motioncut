
expenses = []
def add_expense():
    name = input("Enter the expense name: ")
    amount = float(input("Enter the expense amount: "))
    expenses.append({"name": name, "amount": amount})
    print(f"Added {name} with amount {amount}\n")

def view_expenses():
    if not expenses:
        print("No expenses recorded.\n")
        return
    print("List of expenses:")
    for idx, expense in enumerate(expenses, 1):
        print(f"{idx}. {expense['name']}: ${expense['amount']}")
    print()

def calculate_total():
    total = sum(expense['amount'] for expense in expenses)
    print(f"Total expenses: ${total}\n")

def main():
    while True:
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Calculate Total")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            calculate_total()
        elif choice == '4':
            print("Exiting the tracker.")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()