print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

tip_calculation = ((tip/100)*bill)
total_calculation = ((tip_calculation+bill)/people)

print(f"Each person should pay: {total_calculation:.2f}")


