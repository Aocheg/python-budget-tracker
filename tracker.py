user_name = "Gabriel"
monthly_income = 9000.00
rent_expense = 2000.25

remaining_balance = monthly_income - rent_expense

user_name = input("Enter your name")
monthly_income = float(input("Enter your monthly income:"))
rent_expense = float(input("Enter your rent expense:"))
remaining_balance = monthly_income - rent_expense

print(f"Hello {user_name}! Your remaining balance is: ${remaining_balance:.2f}")

