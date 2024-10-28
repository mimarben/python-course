import random as rd 

with open('./file1.txt', 'w+') as file1:
    for _ in range(100):
        file1.write(f"{rd.randint(1, 100)}\n")
    
with open('./file2.txt', 'w+') as file2:
    for _ in range(100):
        file2.write(f"{rd.randint(1, 100)}\n")

file1_list = []
file2_list = []

with open('./file1.txt', 'r') as file1:
    file1_list = file1.readlines()
    
with open('./file2.txt', 'r') as file2:
    file2_list = file2.readlines()
    
overlap = [int(n) for n in file1_list if n in file2_list]

print(overlap)