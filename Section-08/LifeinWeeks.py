def life_in_weeks(age):
    return (90-age) * 52
age = int(input('Enter your age: '))

print (f"You have {life_in_weeks(age)} weeks left.")

# Alternative solution using string formatting:
print ('You have '+ str(life_in_weeks(age)) + ' weeks left.')




def life_in_weeks_v2(age):
    years_remaining = 90 - age
    weeks_remaining = years_remaining * 52
    print(f"You have {weeks_remaining} weeks left.")
 
 
life_in_weeks(12)