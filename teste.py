def calculate_net_pay():
    hourly_wage = float(input("What is your hourly wage? "))
    hours_worked = float(input("How many hours did you work? "))
    
    gross_pay = hourly_wage * hours_worked
    
    # Tax rates (these are just placeholders)
    federal_tax_rate = 0.1
    state_tax_rate = 0.05
    social_security_rate = 0.062
    
    federal_tax = gross_pay * federal_tax_rate
    state_tax = gross_pay * state_tax_rate
    social_security = gross_pay * social_security_rate
    
    net_pay = gross_pay - (federal_tax + state_tax + social_security)
    
    print(f"\nGross Pay: ${gross_pay:.2f} ({hours_worked} hours @ ${hourly_wage}/hr)")
    print(f"Federal tax: ${federal_tax:.2f}")
    print(f"State tax: ${state_tax:.2f}")
    print(f"Social security: ${social_security:.2f}")
    print(f"Net pay: ${net_pay:.2f}")
    
    return []  # Return an empty list of transactions

def enter_revenue_or_expense():
    transactions = []
    while True:
        transaction_name = input("Enter transaction name: ")
        amount = float(input("Enter amount (use negative sign for expense): "))
        transactions.append((transaction_name, amount))
        another = input("Another? (Y/N): ")
        if another.lower() != 'y':
            break
    return transactions

"""def show_discretionary_income(revenues, expenses):
    total_revenue = sum(revenue for _, revenue in revenues)
    total_expense = sum(abs(expense) for _, expense in expenses)  # Take absolute value of expense
    discretionary_income = total_revenue - total_expense
    print(f"\nTotal Revenue: ${total_revenue:.2f}")
    print(f"Total Expenses: ${total_expense:.2f}")
    print(f"Discretionary Income: ${discretionary_income:.2f}")"""

def show_discretionary_income(revenues, expenses):
    total_revenue = sum(revenue for _, revenue in revenues)
    total_expense = sum(expense for _, expense in expenses)
    discretionary_income = total_revenue - total_expense  # Subtract expenses from revenue
    print(f"\nTotal Revenue: ${total_revenue:.2f}")
    print(f"Total Expenses: ${total_expense:.2f}")
    print(f"Discretionary Income: ${discretionary_income:.2f}")

print("Welcome to My Finance!")

# Define a dictionary to map choices to corresponding functions
menu_options = {
    '1': calculate_net_pay,
    '2': enter_revenue_or_expense,
    '3': lambda: show_discretionary_income([transaction for transaction in transactions if transaction[1] > 0], [transaction for transaction in transactions if transaction[1] < 0]),
    '4': lambda: print("Thanks for using My Finance!")
}

transactions = []

while True:
    print("\n1-Calculate net pay\n2-Enter revenue or expense\n3-Show discretionary income\n4-Exit")
    choice = input("Choice: ")

    # Use the dictionary to call the corresponding function based on user's choice
    selected_option = menu_options.get(choice)
    if selected_option:
        if choice == '3':
            selected_option()
        else:
            transactions.extend(selected_option())
    else:
        print("Invalid choice. Please choose again.")
