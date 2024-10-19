appl=(input("enter appliance name"))
cost=float(input("entercost"))
if cost>=1000:
  warr=.10*cost
else:
  warr=.05*cost
total=cost*warr
print(f"Appliance Name: {appl}, Cost: ${cost:.2f}, Warranty: ${warr:.2f}, Total: ${total:.2f}")