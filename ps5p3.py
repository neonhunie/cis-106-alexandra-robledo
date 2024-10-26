cd = int(input("Enter CD amount: "))
maturity = int(input("Enter maturity years: "))

if cd > 100000 and maturity == 5:
    intrate = 0.06
elif 50000 <= cd <= 100000 and maturity == 10:
    intrate = 0.05
else:
    intrate = 0.02

firstyearint = cd * intrate
print(f"First year interest: ${firstyearint:.2f}, CD: ${cd:.2f}, Maturity: {maturity} years")

