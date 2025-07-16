#Third Assignment

import pymongo
from pymongo import MongoClient
from datetime import datetime
import re
from bson.objectid import ObjectId


# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["ThirdAssign"] 
collection = db["thirdAssignDB"] 

class Expense:
    
    def __init__(self, description, amount, date):
        self.description = description
        self.amount = amount
        self.date = date

    def to_dict(self):
        return {
            "description": self.description,
            "amount": self.amount,
            "date": self.date
        }

class ExpenseTracker:
    
    def __init__(self):
        self.expenses = collection 

    def add_expense(self):
        description = input("\nEnter expense description: ")
        
        while True:
            try:
                amount = float(input("Enter expense amount: "))
                if amount <= 0:
                    print("Amount must be a positive number!")
                else:
                    break
            except ValueError:
                print("Invalid amount! Please enter a numeric value.")
        
        while True:
            date = input("Enter date (YYYY-MM-DD): ")
            if re.match(r"^\d{4}-\d{2}-\d{2}$", date):
                try:
                    datetime.strptime(date, "%Y-%m-%d")
                    break
                except ValueError:
                    print("Invalid date! Please enter a valid date.")
            else:
                print("Invalid format! Please use YYYY-MM-DD.")

        new_expense = Expense(description, amount, date)
        self.expenses.insert_one(new_expense.to_dict())
        print("\n Expense added successfully!")

    def view_expenses(self):
        print("\n--- Your Expenses ---")
        all_expenses = list(self.expenses.find())

        if not all_expenses:
            print("No expenses recorded yet!")
            return

        for expense in all_expenses:
            print(f"ID: {expense['_id']}, Description: {expense['description']}, Amount: {expense['amount']}, Date: {expense['date']}")

    def view_total_expenses(self):
        total = sum(expense["amount"] for expense in self.expenses.find())
        print(f"\n Total Expenses: ${total:.2f}")

    def delete_expense(self):
        self.view_expenses()
        expense_id = input("\nEnter the ID of the expense to delete: ")

        try:
            result = self.expenses.delete_one({"_id": ObjectId(expense_id)})
            if result.deleted_count > 0:
                print("\n Expense deleted successfully!")
            else:
                print("\n No expense found with that ID!")
        except Exception as e:
            print(f" Invalid ID format! Error: {e}")

    def menu(self):
        while True:
            print("\n Personal Expense Tracker")
            print("1. Add New Expense")
            print("2. View All Expenses")
            print("3. View Total Expenses")
            print("4. Delete an Expense")
            print("5. Exit")

            try:
                choice = int(input("\nEnter your option: "))
                if choice == 1:
                    self.add_expense()
                elif choice == 2:
                    self.view_expenses()
                elif choice == 3:
                    self.view_total_expenses()
                elif choice == 4:
                    self.delete_expense()
                elif choice == 5:
                    print("\n👋 Exiting... Have a great day!")
                    break
                else:
                    print("Invalid choice! Please select a number between 1-5.")
            except ValueError:
                print("Invalid input! Please enter a number.")
                
if __name__ == "__main__":
    tracker = ExpenseTracker()
    tracker.menu()
