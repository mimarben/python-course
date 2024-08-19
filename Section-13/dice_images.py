from random import randint

dice_iamges=["0️⃣","1️⃣","2️⃣","3️⃣","4️⃣","5️⃣","6️⃣"]

dice_numer= randint(0,len(dice_iamges)-1)
print(dice_iamges[dice_numer])