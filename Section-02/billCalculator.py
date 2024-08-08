total_bill=float(input("What is the total bill amount?"))
total_tip_percentage=float(input("What is the tip percentage?"))
total_persons=int(input("How many people are sharing the bill?"))

total_tip_amount=float(total_bill) * float(total_tip_percentage) / 100
final_amount=float(total_bill) + total_tip_amount
amount_per_person=final_amount / total_persons

print(f"Total tip amount: {round(total_tip_amount,2)} €")
print(f"Final amount to be paid: {round(final_amount,2)} €")
print(f"Amount per person: {round(amount_per_person,2)} €")

