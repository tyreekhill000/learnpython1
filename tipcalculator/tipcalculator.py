print("Welcome to the tip calculator")
people = input("People going all together: ")
bill = input("Total bill: ")
tip = input("percentage of tip: ")
people_int = int(people)
bill_float = float(bill)
tip_float = float(tip)
tip_amount = ((tip_float/100)*bill_float)
total_bill_with_tip = (tip_amount + bill_float)
share_amount = (total_bill_with_tip / people_int)
print(round(share_amount,2))