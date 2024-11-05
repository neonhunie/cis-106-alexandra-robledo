start=1
control= str(input(" enter yes if you would like to run this program "))
x=0
while control=="yes":
  name=str(input(" enterstudents name "))
  midterm=float(input(" enter midterm grade "))
  final=float(input(" enter final grade "))
  average= (midterm + final)/2
  print(name, " has an average of", average)
  x=x+1
  control=str(input(" enter yes if you would like to run this program"))
print("you have run this program", x, "times")