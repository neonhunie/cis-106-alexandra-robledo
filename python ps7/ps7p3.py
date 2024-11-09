f=open("ps7p3.txt","r")
lastname=f.readline()
totalbonus=0
while lastname !="":
  salary=float(f.readline())
  if salary>=100000:
    bonus=.20
  elif salary>=50000:
    bonus=.15
  else: 
    bonus=.10
  bonusamt=salary*bonus
  print (f'{lastname} Salary is {salary:.2f} bonus is {bonus:.2f}bonus rate is {bonusamt:.2f}')
  totalbonus = totalbonus + bonusamt
  lastname= f.readline()
print ("Total Bonus is", totalbonus)