import os

class Expense:
    def __init__(self, amount, category, date, description):
        self.amount = amount
        self.category = category
        self.date = date
        self.description = description


class ExpenseTracker:
    def __init__(self):
        self.expenses = []
        self.expense_array = []

    def add_expense(self):
        amount = float(input("Enter the expense amount: "))
        category = input("Enter the expense category: ")
        date = input("Enter the expense date (YYYY-MM-DD): ")
        description = input("Enter the expense description: ")

        expense = Expense(amount, category, date, description)
        self.expenses.append(expense)
        self.expense_array.append(f"Amount: {amount}, Category: {category}, Date: {date}, Description: {description}")
        print("Expense added successfully!")

    def generate_report(self):
        total_expenses = len(self.expenses)
        total_amount = sum(expense.amount for expense in self.expenses)
        average_amount = total_amount / total_expenses if total_expenses > 0 else 0

        report = f"Total expenses: {total_expenses}\n"
        report += f"Total amount spent: {total_amount}\n"
        report += f"Average amount per expense: {average_amount}\n"

        for expense in self.expense_array:
            report += f"{expense}\n"

        return report

    def save_expenses_to_file(self, file_name):
        with open(file_name, 'w') as file:
            for expense in self.expense_array:
                file.write(expense + '\n')
        print(f"Expense details saved to {file_name}.")

    def load_expenses_from_file(self, file_name):
        if os.path.exists(file_name):
            with open(file_name, 'r') as file:
                self.expense_array = [line.strip() for line in file]
            print(f"Expense details loaded from {file_name}.")
        else:
            print("File does not exist. No expenses loaded.")


# Example usage:
tracker = ExpenseTracker()

while True:
    choice = input("Enter 'A' to add an expense, 'R' to generate a report, 'S' to save expenses, 'L' to load expenses, or 'Q' to quit: ")
    if choice.upper() == "A":
        tracker.add_expense()
    elif choice.upper() == "R":
        report = tracker.generate_report()
        print(report)
    elif choice.upper() == "S":
        file_name = input("Enter the file name to save the expenses: ")
        tracker.save_expenses_to_file(file_name)
    elif choice.upper() == "L":
        file_name = input("Enter the file name to load the expenses: ")
        tracker.load_expenses_from_file(file_name)
    elif choice.upper() == "Q":
        break
    else:
        print("Invalid choice! Please try again.")

print("Program terminated.")
