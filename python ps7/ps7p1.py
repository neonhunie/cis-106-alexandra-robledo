loop=(input("Y if you would like to loop "))
while loop=="Y":
  p=float(input("enter the principle amount"))
  r=float(input("enter the interest rate in decimal form"))
  total_i=0
  print ("\n year", "begining balance","ending balance")
  for y in range (1,6,1):
    i= p*r
    eb= i+p 
    print ("\n,y,","{:.2f}".format(p),"{:.2f}".format(eb))
    p=eb 
    total_i=total_i+i
  print ("\n Total interest earned is:","{:.2f}".format(total_i))
  loop=(input("Y if you would like to loop "))