def calculate_mpg(miles, gallons):
  if gallons == 0:
      return 0.0  
  return miles / gallons
trip_count = 0

while True:
  destination = input("Enter the destination city (or 'stop' to end): ")
  if destination.lower() == 'stop':
      break 

  try:
      miles = float(input("Enter the miles traveled: "))
      gallons = float(input("Enter the gallons used: "))
  except ValueError:
      print("Invalid input. Please enter numeric values for miles and gallons.")
      continue  


  mpg = calculate_mpg(miles, gallons)


  print(f"Destination: {destination}, Miles Traveled: {miles}, MPG: {mpg:.2f}")
    
  trip_count += 1
    
print(f"Total number of trips: {trip_count}")
