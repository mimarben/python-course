import random as rnd
lower_bound=0
upper_bound=1000

random_list = [rnd.randint(lower_bound, upper_bound) for _ in range(100)]

print ("Original List:", random_list)

total_examen_score = sum(random_list)
print ("Total Exam Score:", total_examen_score)

sum_score =0  
for score in random_list:
  sum_score += score

print ("Score:", sum_score)

print("max value: ",max(random_list))

max_value=0
for score in random_list:
  if score > max_value:
    max_value=score

print("max value: ", max_value)