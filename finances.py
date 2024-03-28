def calculate_withholding(wage, time_worked):
    # Tax rates
    federal_tax_rate = 0.10
    state_tax_rate = 0.05
    social_security_rate = 0.062

    # Calculate withholding amounts
    gross_pay = wage * time_worked
    federal_tax = gross_pay * federal_tax_rate
    state_tax = gross_pay * state_tax_rate
    social_security = gross_pay * social_security_rate

    withholding = federal_tax + state_tax + social_security
    net_pay = gross_pay - withholding

    return net_pay, withholding


def track_monthly_costs_and_income():
    total_income = 0
    total_expenses = 0

    while True:
        transaction_type = input("Enter transaction type (income/expense): ").lower()
        amount = float(input("Enter amount: "))

        if transaction_type == "income":
            total_income += amount
        elif transaction_type == "expense":
            total_expenses += amount
        else:
            print("Invalid transaction type. Please enter either 'income' or 'expense'.")

        another_transaction = input("Another? (Y/N): ")
        if another_transaction.upper() != "Y":
            break

    return total_income, total_expenses


def calculate_discretionary_income(total_income, total_expenses):
    discretionary_income = total_income - total_expenses
    return discretionary_income


def main():
    while True:
        print("\nMenu:")
        print("1. Calculate net pay and report withholding amounts")
        print("2. Track monthly costs and income")
        print("3. Report monthly discretionary income")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            wage = float(input("Enter hourly wage: "))
            time_worked = float(input("Enter hours worked: "))
            net_pay, withholding = calculate_withholding(wage, time_worked)
            print(f"Net pay: ${net_pay:.2f}")
            print(f"Withholding: ${withholding:.2f}")

        elif choice == "2":
            total_income, total_expenses = track_monthly_costs_and_income()
            print(f"Total income: ${total_income:.2f}")
            print(f"Total expenses: ${total_expenses:.2f}")

        elif choice == "3":
            total_income, total_expenses = track_monthly_costs_and_income()
            discretionary_income = calculate_discretionary_income(total_income, total_expenses)
            print(f"Monthly discretionary income: ${discretionary_income:.2f}")

        elif choice == "4":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 4.")


if __name__ == "__main__":
    main()
