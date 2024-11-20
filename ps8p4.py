def determine_pay_rate(job_code):
  if job_code.upper() == 'L':
      return 25
  elif job_code.upper() == 'A':
      return 30
  elif job_code.upper() == 'J':
      return 50
  else:
      return 0

total_gross_pay = 0

while True:
  last_name = input("Enter the employee's last name (or 'stop' to end): ")
  if last_name.lower() == 'stop':
      break

  job_code = input("Enter the job code (L, A, J): ")
  try:
      hours_worked = float(input("Enter the hours worked: "))
  except ValueError:
      print("Invalid input. Please enter a valid number for hours.")
      continue

  pay_rate = determine_pay_rate(job_code)
  if pay_rate == 0:
      print("Invalid job code. Please enter L, A, or J.")
      continue

  if hours_worked > 40:
      gross_pay = (40 * pay_rate) + ((hours_worked - 40) * pay_rate * 1.5)
  else:
      gross_pay = hours_worked * pay_rate

  print(f"Last Name: {last_name}, Gross Pay: ${gross_pay:.2f}")
  total_gross_pay += gross_pay

print(f"Total Gross Pay for all employees: ${total_gross_pay:.2f}")
