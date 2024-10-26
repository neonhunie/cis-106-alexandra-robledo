tickets=int(input(" enter number of tickets"))
if tickets>=25:
  price=50
elif 10<=tickets<=24:
  price=60
elif 5<=tickets<=9:
  price=70
else:
  price=75
cost=tickets*price
print(f"Number of tickets: {tickets}, Price per ticket: ${price:.2f}, Total cost: ${cost:.2f}")