# Simple Interest
P = float(input("Enter principal amount: "))
R = float(input("Enter interest rate (%): "))
T = float(input("Enter time (years): "))

A = P * (1 + (R / 100) * T)
print("Simple Interest:", A)

# Compound Interest
P = float(input("Enter principal amount: "))
R = float(input("Enter interest rate (%): "))
T = float(input("Enter time (years): "))
n = int(input("Enter number of times interest is compounded per year: "))

A = P * (1 + R / (100 * n)) ** (n * T)
print("Compound Interest:", A)

# Annuity Plan
PMT = float(input("Enter annuity payment: "))
R = float(input("Enter interest rate (%): "))
T = float(input("Enter time (years): "))
n = int(input("Enter number of times interest is compounded per year: "))

A = PMT * (((1 + R / (100 * n)) ** (n * T) - 1) / (R / (100 * n)))
print("Annuity Plan:", A)
