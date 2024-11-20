def compute_tuition(credit_hours, district_code):
  if district_code.upper() == 'I':
      return credit_hours * 250
  elif district_code.upper() == 'O':
      return credit_hours * 550
  else:
      return 0

total_tuition = 0

while True:
  last_name = input("Enter the student's last name (or 'stop' to end): ")
  if last_name.lower() == 'stop':
      break

  try:
      credit_hours = int(input("Enter the credit hours: "))
  except ValueError:
      print("Invalid input. Please enter a valid number for credit hours.")
      continue

  district_code = input("Enter the district code (I for In-District, O for Out-of-District): ")

  tuition = compute_tuition(credit_hours, district_code)
  if tuition == 0:
      print("Invalid district code. Please enter I or O.")
      continue

  print(f"Student Name: {last_name}, Tuition Owed: ${tuition:.2f}")
  total_tuition += tuition

print(f"Total Tuition Owed for all students: ${total_tuition:.2f}")
