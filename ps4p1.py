quant=int(input("Enter quantity: "))
if quant>=1000:
  unit=3
else:
  unit=5
extprice=quant*unit
tax=.07*extprice
total=extprice+tax
print(f"Quantity: {quant}, Unit Price: ${unit:.2f}, Extended Price: ${extprice:.2f}, Tax: ${tax:.2f}, Total: ${total:.2f}")