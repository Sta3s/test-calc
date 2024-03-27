from functions import calculate_monthly_payment

print("Welcome to the Mortgage Calculator!")
amount = float(input("Enter the loan amount: "))
annual_interest_rate = float(input("Enter the annual interest rate (e.g., 5 for 5%): "))
years = int(input("Enter the loan term in years: "))

monthly_payment = calculate_monthly_payment(amount, annual_interest_rate, years)

print("\nYour monthly payment will be: €{:.2f}".format(monthly_payment))

# Happy-Path
# 1. It is known that the monthly wage is the result of principal * monthly_interest_rate / (1 - (1 + monthly_interest_rate) ** -months) if we enter
# loan amount 500, annual interest rate 5 and 2 years, we get €21.94

# Use-Case
# 1. It is known that the monthly wage is the result of principal * monthly_interest_rate / (1 - (1 + monthly_interest_rate) ** -months) if we enter
# loan amount 1, annual interest rate 5 and 2 years, we get €0.04
# 2. It is known that the monthly wage is the result of principal * monthly_interest_rate / (1 - (1 + monthly_interest_rate) ** -months) if we enter
# loan amount 900, annual interest rate 5.5 and 2 years, we get €39.69
# 3. It is known that the monthly wage is the result of principal * monthly_interest_rate / (1 - (1 + monthly_interest_rate) ** -months) if we enter
# loan amount 1000, annual interest rate 5.5 and 2.26, we will get an error
# 4. It is known that the monthly wage is the result of principal * monthly_interest_rate / (1 - (1 + monthly_interest_rate) ** -months) if we enter
# Loan amount 10, annual interest rate 10 and 10 years, then we get €0.13
# 5. It is known that the monthly wage is the result of principal * monthly_interest_rate / (1 - (1 + monthly_interest_rate) ** -months) if we enter
# Loan amount 0.5, annual interest rate 10 and 10 years, then we get €0.01

# Edge-Case
# 1. It is known that the monthly wage is the result of principal * monthly_interest_rate / (1 - (1 + monthly_interest_rate) ** -months) if we enter
# loan amount 0, annual interest rate 10 and 10 years, then we get €0.00
# 2. It is known that the monthly wage is the result of principal * monthly_interest_rate / (1 - (1 + monthly_interest_rate) ** -months) if we enter
# loan amount -1, annual interest rate -8 and 10 years, then we will get €-0.01
# 3. It is known that the monthly wage is the result of principal * monthly_interest_rate / (1 - (1 + monthly_interest_rate) ** -months) if we enter
# loan amount 9.654645, annual interest rate of 8 and 10 years, then we get €0.12
# 4. It is known that the monthly wage is the result of principal * monthly_interest_rate / (1 - (1 + monthly_interest_rate) ** -months) if we enter
# loan amount TWENTY, we will get an error
# 5. It is known that the monthly wage is the result of principal * monthly_interest_rate / (1 - (1 + monthly_interest_rate) ** -months) if we enter
# loan amount 99999, annual interest rate -8212.6 and 10 years then we get €-684376.49