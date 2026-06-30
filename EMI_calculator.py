# EMI Calculator
def calculate_emi(principal, annual_rate, years):
    monthly_rate = annual_rate / (12 * 100)
    months = years * 12

    emi = (principal * monthly_rate * (1 + monthly_rate) ** months) / \
          ((1 + monthly_rate) ** months - 1)

    return emi

loan_amount = float(input("Enter Loan Amount: "))
interest_rate = float(input("Enter Annual Interest Rate (%): "))
tenure = int(input("Enter Loan Tenure (Years): "))

emi = calculate_emi(loan_amount, interest_rate, tenure)

print(f"\nMonthly EMI: ₹{emi:.2f}")