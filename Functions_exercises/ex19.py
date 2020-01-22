#Functions and variables

def cheese_and_crackers(cheese_count,box_of_crackers):
    print(f"You have {cheese_count} cheeses")
    print(f"you have {box_of_crackers} Box of crackers")
    print("Let party then!")

print("we can just give function numbers directly:")
cheese_and_crackers(20,30)

print("OR we can use variable")
amount_of_cheese=30
box_of_crackers=40

cheese_and_crackers(amount_of_cheese,box_of_crackers)

print("And we  can combine variable and math")
cheese_and_crackers(amount_of_cheese*10,box_of_crackers+10)