# Write your solution here
number = int(input("Please type in a number: "))
text = "This number is smaller than"
if number < 10:
    print(f"{text} 1000")
    print(f"{text} 100")
    print(f"{text} 10")
elif number < 100:
    print(f"{text} 1000")
    print(f"{text} 100")
elif number < 1000:
    print(f"{text} 1000")
print("Thank you!")