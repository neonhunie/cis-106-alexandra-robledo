print ("enter quantity")
quantity= int(input ())
if quantity>10000:
  price=10
elif 5000 <= quantity <= 10000:
  price=20
else: 
  price=30
extprice=quantity*price
tax=7/100*extprice
total=extprice+tax
print(f"Your extended price is: ${extprice:.2f}, your tax is: ${tax:.2f}, and your total is: ${total:.2f}")