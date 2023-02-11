fahrenheit = float(input("Please type in a temperature (F): "))
degre = (fahrenheit - 32) / 1.8
print(f"{fahrenheit} degrees Fahrenheit equals {degre} degrees Celsius")
if degre < 0:
    print(f"Brr! It's cold in here!")