import random as rnd
# Rock Paper Scissors ASCII Art
# Rock
rock="""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper="""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissors="""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
options = [rock, paper, scissors]
options_names = ['rock', 'paper', 'scissors']
user_option = int(input("Choose your option (rock (0), paper (1), scissors(2)): "))
if isinstance(user_option, int) and user_option >= 0 and user_option <= 2:
  print(f"You chose {options_names[user_option]}\n", options[user_option])
  auto_option = rnd.randint(0, 2)
  if auto_option == user_option:
    print("Computer chose\n", options[auto_option])
    print("It's a tie!")
  elif (auto_option == 0 and user_option == 1) or (auto_option == 1 and user_option == 2) or (auto_option == 2 and user_option == 0):
    print(f"Computer chose {options_names[auto_option]}\n", options[auto_option])
    print("You win!")
  else:
    print(f"Computer chose {options_names[auto_option]}\n", options[auto_option])
    print("You lose!")
else:
  print ("please enter a valid integer number between 0 and 2!")

