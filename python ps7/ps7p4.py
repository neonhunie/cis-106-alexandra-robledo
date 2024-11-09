f = open("ps7p4.txt", "r")
item = f.readline()
totalprices = 0
count = 0

while item != "":
    quantity = int(f.readline())
    price = float(f.readline())
    extprice = quantity * price
    print(f"item: {item.strip()} quantity: {quantity} unit price: ${price:.2f} total: ${extprice:.2f}")

    count = count + 1
    totalprices = totalprices + extprice
    item = f.readline()

print("Total money spent:", totalprices, "Number of items:", count, "Average cost per order:", totalprices / count)
f.close()