height = int(input("Enter your height (in centimeter): "))
if height>120:
  print("You can ride the rollercoaster!")
  age = int(input("Enter your age: "))
  if age <= 12:
    bill = 5
    print("Congratulations! You're a child ticket!")
  elif age > 12 and age <= 18:
    bill =7
    print("Congratulations! You're an adult ticket!")
  else:
    bill = 12
    print("Congratulations! You're a senior ticket!")

  wants_photo = input("Do you want a photo(yes/no): ")
  if wants_photo.lower() == "yes":
      bill += 3
  print("Your final bill is: $", bill)

else:
  print("Sorry, you're too short to ride the rollercoaster.")