
item = input("What item would you like to buy?: ")
price = float (input("What is the price?: "))
quantity = int(input("How many would you like to buy?: "))
total = price * quantity

print(f"You have bought {quantity} x {item}/s")
print(f"Your total is ₱{total}")



operator = input("Enter an operator( + - * /) : ")
num1 = float(input("Enter the 1st number: "))
num2 = float(input("Enter the 2nd number: "))

if operator == "+":
    result = num1 + num2
    print(round(result))
elif operator == "-":
    result = num1 - num2
    print(round(result))
elif operator == "*":
    result = num1 * num2
    print(round(result))
elif operator == "/":
    result = num1 / num2
    print(round(result))
else:
    print(f"{operator}is not a valid operator")


weight = float(input("Enter your weight: "))
unit = input("Kilogram or Pounds? (K or L): ")

if unit == "K":
    weight = weight * 2.205
    unit = "Lbs."
elif unit == "L":
    weight = weight / 2.205
    unit = "Kgs."
else:
    print(f"{unit} was not valid")

print(f"Your weight is: {round(weight, 1)} {unit}")

#Python compound interest calculator

principle = 0
rate = 0
time = 0

while principle <= 0:
      principle = float(input("Enter the principle amount: "))
      if principle <= 0:
          print("Principle can't be less than or equal to zero")

print(principle)

while rate <= 0:
      rate = float(input("Enter the interest rate: "))
      if rate <= 0:
          print("Interest rate can't be less than or equal to zero")

while time <= 0:
      time = int(input("Enter the time in years: "))
      if time <= 0:
          print("Time can't be less than or equal to zero")

total = principle * pow((1 + rate / 100), time)
print(f"Balance after {time} year/s: {total:.2f}")


