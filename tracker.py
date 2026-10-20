user_name = "Gabriel"
monthly_income = 12000.00
rent_expenses = 1200.75

remaining_balance = monthly_income - rent_expenses

user_name = input("Enter your name")
monthly_income = float(input("Enter your monthly income:"))
rent_expense = float(input("Enter your rent expenses:"))
remaining_balance = monthly_income - rent_expenses

print(f"Hello {user_name}! Your remaining balance is: ${remaining_balance:.2f}")

