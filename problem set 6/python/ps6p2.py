start=1
x=0
control= str(input(" enter yes if you would like to run this program "))
while control=="yes":
  lastname=str(input(" enter employees last name "))
  hours=float(input(" enter hours worked "))
  rate=float(input(" enter employees rate "))
if hours>40:
  grosspay=40*rate+(hours-40)*rate*1.5
else: grosspay= hours*rate  
print(lastname, " has gross pay of", grosspay)
x=x+1
control=str(input(" enter yes if you would like to run this program"))
print("you have run this program", x, "times")