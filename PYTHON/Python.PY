# Simple Interest Calculator

principal = float(input("Enter principal amount: "))
rate = float(input("Enter rate of interest: "))
time_period = float(input("Enter time (in years): "))

simple_interest = (principal * rate * time_period) / 100

print("Simple Interest:", simple_interest)
