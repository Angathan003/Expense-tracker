class Expense:
    def __init__(self, amount, category, date, description):
        self.amount = amount
        self.category = category
        self.date = date
        self.description = description


class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self):
        amount = float(input("Enter the expense amount: "))
        category = input("Enter the expense category: ")
        date = input("Enter the expense date (YYYY-MM-DD): ")
        description = input("Enter the expense description: ")

        expense = Expense(amount, category, date, description)
        self.expenses.append(expense)
        print("Expense added successfully!")

    def generate_report(self):
        total_expenses = len(self.expenses)
        total_amount = sum(expense.amount for expense in self.expenses)
        average_amount = total_amount / total_expenses if total_expenses > 0 else 0

        report = f"Total expenses: {total_expenses}\n"
        report += f"Total amount spent: {total_amount}\n"
        report += f"Average amount per expense: {average_amount}\n"

        return report


# Example usage:
tracker = ExpenseTracker()

while True:
    choice = input("Enter 'A' to add an expense or 'R' to generate a report (or 'Q' to quit): ")
    if choice.upper() == "A":
        tracker.add_expense()
    elif choice.upper() == "R":
        report = tracker.generate_report()
        print(report)
    elif choice.upper() == "Q":
        break
    else:
        print("Invalid choice! Please try again.")

print("Program terminated.")
