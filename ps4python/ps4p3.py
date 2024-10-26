books = int(input("Enter number of books: "))
price = float(input("Input price of books: "))
totalcost = price * books
if totalcost > 50:
    print(f"Your total cost is ${totalcost:.2f}")
else:
    print(f"Your total cost is ${(totalcost + 25):.2f}")