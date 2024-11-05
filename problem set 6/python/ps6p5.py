start=1
control= str(input(" enter yes if you would like to run this program "))
ds= 0
while control=="yes":
  price=float(input("enter price of item"))
  quantity=int(input("enter quantity"))
  extprice=price*quantity
  disc = 0
  if extprice>5000:
    disc=extprice*0.25
  else:
    disc=extprice*.10
  ds =disc+ds
  total=extprice-disc
  print ("your discount is: $", disc)
  print ("your extended price is: $", extprice)
  print ("your total is: $",total)

  control= str(input(" enter yes if you would like to run this program "))
print ("youre total discount is: $", ds)

