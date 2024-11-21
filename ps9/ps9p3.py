def highlow(students,examscore):
  high=examscore[0]
  low=examscore[0]
  whichhigh=0
  whichlow=0
  for i in range(0,len(examscore)-1,1):
    if examscore[i]>high:
      high=examscore[i]
      whichhigh=i
    if examscore[i]<low:
      low=examscore[i]
      whichlow=i
  print(f"The highest score is",high, "and the student is",students[whichhigh])
  print (f"The lowest score is",low, "and the student is",students[whichlow])

f=open("ps9ex.txt","r")
name= f.readline().rstrip('\n')
students=[]
examscore=[]

while name !="":
  students.append(name)
  exam=float(f.readline())
  examscore.append(exam)
  name= f.readline().rstrip('\n')

print (students)
print(examscore)
highlow(students,examscore)



















