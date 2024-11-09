f = open("ps7p5.txt", "r")
sumoftuition = 0
totalstudents = -1
lastname = "temp"
lastname = f.readline()
while lastname != "":
  totalstudents += 1
  district = f.readline()
  credits = f.readline()
  cpc = 0
  if district == "i":
    cpc = 250
  else:
    cpc = 500

  tuition = float(credits) * float(cpc)
  print("Last Name: ", lastname, "Credits Taken ", credits, "Tuition: ",
        tuition)
  lastname = f.readline()
  sumoftuition += tuition

print("Total Students: ", totalstudents, "Total Tuition: ", sumoftuition)
