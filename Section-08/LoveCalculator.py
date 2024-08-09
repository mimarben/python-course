
true_list = list("true")
love_list = list("love")
def calculate_love_score(man, woman):
    score_love = 0
    score_true = 0
    man_list= list(man)
    woman_list= list(woman)
    copule_list= man_list+woman_list
    print (copule_list)
    for letter in copule_list:
        times_true= true_list.count(letter)
        times_love= love_list.count(letter)
        if times_love > 0:
            print(f"The letter '{letter}' has been appeared {times_love} times in love")
            score_love += times_love
        if times_true>0:
            print(f"The letter '{letter}' has been appeared {times_true} times in true")
            score_true += times_true
    
    return ( str(score_true) +str(score_love)) 

man_name = input("Insert man name: ").lower()
woman_name = input("Insert woman name: ").lower()


total_score = calculate_love_score(man_name, woman_name)

print(f"Your love score is {total_score}")