
"""
personal_expense_tracker.py

Author  : Harish Varma
Version : 1.0.0

"""


import csv
import sys
import logging
import argparse
from datetime import datetime
from pathlib import Path

# a list to store all expenses
expenses = []
# a variable to store the monthly budget
monthly_budget = 0.0

# ─────────────────────────────────────────────────────────────────────────────
# 1. ADD EXPENSE
# ─────────────────────────────────────────────────────────────────────────────
def add_expense():
    # ask the user for details
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category (Food, Travel, Housing, Health, Entertainment, Shopping, Others ): ")
    amount = input("Enter amount spent: ")
    description = input("Enter description: ")

    # convert amount to number
    try:
        amount = float(amount)
    except:
        print("Amount must be a number!")
        return

    # make a dictionary
    expense = {
        "date": date,
        "category": category,
        "amount": amount,
        "description": description
    }

    # put the dictionary into the list
    expenses.append(expense)
    print("Expense added!\n")

# ─────────────────────────────────────────────────────────────────────────────
# 2. VIEW EXPENSES
# ─────────────────────────────────────────────────────────────────────────────
def view_expenses():
    if len(expenses) == 0:
        print("No expenses yet.\n")
        return

    print("\n--- Expenses ---")
    for exp in expenses:
        # check if all details are there
        if exp["date"] and exp["category"] and exp["amount"] and exp["description"]:
            print("Date:", exp["date"], "| Category:", exp["category"], "| Amount:", exp["amount"], "| Description:", exp["description"])
        else:
            print("Incomplete expense found, skipping...")
    print()

# ─────────────────────────────────────────────────────────────────────────────
# 3. SET BUDGET  &  TRACK BUDGET
# ─────────────────────────────────────────────────────────────────────────────
def set_budget():
    global monthly_budget
    budget = input("Enter your monthly budget: ")
    try:
        monthly_budget = float(budget)
        print("Budget set to", monthly_budget, "\n")
    except:
        print("Budget must be a number!\n")

# 3b. Track budget
def track_budget():
    if monthly_budget == 0:
        print("No budget set yet.\n")
        return

    total = 0
    for exp in expenses:
        total += exp["amount"]

    print("Total spent so far:", total)
    if total > monthly_budget:
        print("You have exceeded your budget!\n")
    else:
        print("You have", monthly_budget - total, "left for the month.\n")

# ─────────────────────────────────────────────────────────────────────────────
# 4. SAVE & LOAD EXPENSES
# ─────────────────────────────────────────────────────────────────────────────
def save_expenses(filename="expenses.csv"):
    with open(filename, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["date", "category", "amount", "description"])
        writer.writeheader()
        writer.writerows(expenses)
    print("Expenses saved!\n")

# 4b. Load expenses
def load_expenses(filename="expenses.csv"):
    global expenses
    try:
        with open(filename, "r") as file:
            reader = csv.DictReader(file)
            expenses = []
            for row in reader:
                row["amount"] = float(row["amount"])  # convert back to number
                expenses.append(row)
        print("Expenses loaded!\n")
    except FileNotFoundError:
        print("No saved file found. Starting fresh.\n")

# ─────────────────────────────────────────────────────────────────────────────
# 5. INTERACTIVE MENU
# ─────────────────────────────────────────────────────────────────────────────
def menu():
    load_expenses()  # load old data when program starts
    while True:
        print("----- Expense Tracker -----")
        print("1. Add expense")
        print("2. View expenses")
        print("3. Set budget")
        print("4. Track budget")
        print("5. Save expenses")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            set_budget()
        elif choice == "4":
            track_budget()
        elif choice == "5":
            save_expenses()
        elif choice == "6":
            save_expenses()
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.\n")

# run the program
menu()
