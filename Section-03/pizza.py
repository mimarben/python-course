print("Welcome to Python pizza ordering system!")
size= input("Enter the size of your pizza (small, medium, large): ")
pepperoni = input("Do you want pepperoni? (yes/no): ")
extra_cheese = input("Do you want extra cheese? (yes/no): ")

bill=0
if size.lower() == "small":
  bill+=10
elif size.lower() == "medium":
  bill+=15
elif size.lower() == "large":
  bill+=20
else:
  print("Please enter a coorrect size (small, medium, large).")

if pepperoni.lower() == "yes":
    if size.lower() == "small":
      bill+=1
    if size.lower() =="medium":
      bill+=3
    if size.lower() == "large":
      bill+=4

if extra_cheese.lower() == "yes":
    if size.lower() == "small":
      bill+=1
    if size.lower() =="medium":
      bill+=3
    if size.lower() == "large":
      bill+=4

print("Your final bill is: $", bill)  