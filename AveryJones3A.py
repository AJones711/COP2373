# Create a program that has the user enter a list of their monthly expenses and calculate the total, highest, and lowest expense.
# When making list user will enter the expense type as well as the amount.
from functools import reduce

def main ():
    # Create the list for the expenses to be stored
    expenses = []

    # Create an infinite while loop that has the user enter an expense type followed by the amount.
    while True:
        expense_type = input("Enter the type of expense or type 'done' to finish: ")
        if expense_type.lower() == 'done':
            break

        amount = float(input(f"Enter the amount for {expense_type}: "))
        expenses.append((expense_type, amount))

    # If loop ends without any expenses entered print "No expenses have been entered."
    if not expenses:
        print("No expenses have been entered.")
        return

    # Calculate total, highest, and lowest expense.
    total_expense = reduce(lambda accumulator, expense: accumulator + expense[1], expenses, 0)
    highest_expense = reduce(lambda accumulator, expense: expense if expense[1] > accumulator[1] else accumulator, expenses)
    lowest_expense = reduce(lambda accumulator, expense: expense if expense[1] < accumulator[1] else accumulator, expenses)

    # Print results.
    print(f"\nTotal Expense: ${total_expense:.2f}")
    print(f"Highest Expense: {highest_expense[0]} - ${highest_expense[1]:.2f}")
    print(f"Lowest Expense: {lowest_expense[0]} - ${lowest_expense[1]:.2f}")

main()