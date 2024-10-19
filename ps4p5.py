last_name=(input("Enter last name: "))
dependents=int(input("Enter number of Dependents: "))
gross_income=float(input("Enter gross income: "))
adj_income=gross_income-dependents*12000
if adj_income>50000:
  tax_rate=.20
else:
  tax_rate=.10
income_tax=adj_income*tax_rate
if income_tax<0:
  income_tax=100
print(f"Last Name: {last_name}, Gross Income: ${gross_income:.2f}, dependents: {dependents}, Adjusted Gross Income: ${adj_income:.2f}, Income Tax: ${income_tax:.2f}")