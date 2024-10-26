print ("enter item to be purchased")
item = input()
print ("enter the quantity")
quantity= int(input ())
if item=="10":
  unitprice=1.00
elif item=="55":
  unitprice=1.00
elif item=="99":
  unitprice=2.00
elif item== "80" or item=="70":
  unitprice=3.00
else:
  unitprice=5.00
price=quantity*unitprice
print ("the item to buy is", item, "\n the unit price is: $","{:.2f}".format(unitprice),"\n the price is: $","{:.2f}".format(price))