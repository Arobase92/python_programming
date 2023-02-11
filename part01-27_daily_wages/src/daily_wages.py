# Write your solution here
wage_hour = float(input("Hourly wage: "))
work_hour = float(input("Hours worked: "))
day = input("Day of the week: ")
daily_wage = wage_hour * work_hour

if day == "Sunday":
    print(f"Daily wages: {daily_wage*2} euros")
else:
    print(f"Daily wages: {daily_wage} euros")