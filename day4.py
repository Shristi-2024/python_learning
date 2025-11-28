# Calculate compound interest
def compound_interest(principal, rate, time, n):
    """
    Calculate compound interest.
    principal : initial amount
    rate      : annual interest rate in decimal (e.g., 0.05 for 5%)
    time      : time in years
    n         : number of times interest is compounded per year
    """
    amount = principal * (1 + rate/n)**(n*time)
    interest = amount - principal
    return amount, interest

# --- Take input from user ---
P = float(input("Enter the principal amount: "))
r = float(input("Enter annual interest rate (in %): ")) / 100   # convert % to decimal
t = float(input("Enter time in years: "))
n = int(input("Enter number of times interest is compounded per year: "))

final_amount, comp_interest = compound_interest(P, r, t, n)

print(f"\nFinal Amount: {final_amount:.2f}")
print(f"Compound Interest: {comp_interest:.2f}")

