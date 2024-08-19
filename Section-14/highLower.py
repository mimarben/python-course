from art import logo, vs
from game_data import data
import random
options=[]

def get_random_data():
    """Returns a random data entry."""
    first_option = random.choice(data)
    while True:
        second_option = random.choice(data)
        if second_option != first_option:
            break
    # TODO: Implement this function to return a random data entry from the provided list.
    # The returned data entry should contain a 'name' and 'country' key.
    return (first_option, second_option)
options = get_random_data()
print(logo)
print(f"Compare A: {options[0]['name']}, a {options[0]['description']} from {options[0]['country']}")
print(vs)
print(f"Compare A: {options[1]['name']}, a {options[1]['description']} from {options[1]['country']}")
answer = input("Who has more followers? Type 'A' or 'B': ")

if answer.lower() == 'a':
    if options[0]['follower_account'] > options[1]['follower_account']:
        print(f"You are correct! {options[0]['name']} has {options[0]['follower_account']} followers.")
    else:
        print(f"Sorry, that's wrong! {options[1]['name']} has {options[1]['follower_account']} followers.")