lastname=input("Enter last name: ")
salary=float(input("Enter salary: "))
joblevel=int(input("Enter job level: "))
if joblevel>=10:
  bonus=.25
elif joblevel>=5 and joblevel<=9:
  bonus=.20
else:
  bonus=.10
bonusamt=salary*bonus
print(f"Last name: {lastname}, Bonus amount: ${bonusamt:.2f}")
