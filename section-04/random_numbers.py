#https://en.wikipedia.org/wiki/Mersenne_Twister


import random as rd

rnd = rd.randint(0,9)
print(f"The secret number is {rnd}")
rdn_1= rd.random()*10
print(f"The secret number is {rdn_1}")
rdn_2 = rd.uniform(0,10)
print(f"The secret number is {rdn_2}") 
