import random as rd
friends = ["Alice", "Bob", "Charlie", "David", "Eve"]
print(rd.choice(friends))
print(rd.sample(friends, 2))
random_index=rd.randint(0, len(friends)-1)
print(friends[random_index])