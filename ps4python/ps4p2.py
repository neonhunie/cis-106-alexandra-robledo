item=str (input ("Enter the item must be A or B:"))
qua=int(input("enter the quantity"))
if item=="A":
  unitprice=10
else:
  unitprice=20
total=qua*unitprice
print (f"item: {item} quantity: {qua} unit price: ${unitprice:.2f} total: ${total:.2f}")