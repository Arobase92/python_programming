# Write your solution here
day = int(input("How many times a week do you eat at the student cafeteria? "))
price_lunch = float(input("The price of a typical student lunch? "))
spend_week = float(input("How much money do you spend on groceries in a week? "))
print()
print(f"Average food expenditure:")
print(f"Daily: {(day * price_lunch + spend_week)/7} euros")
print(f"Weekly: {day*price_lunch+spend_week} euros")