print('Welcome to the tip calculator.')

total_bill = float(input("What is the total bill? $"))
people_count = float(input("How many people to split the bill? "))
tip_percentage = float(input("What percentage tip would you like to give? 10, 12 or 15? "))
tip_amount = (total_bill*tip_percentage/100) / people_count
print(f"Each person should pay: ${tip_amount}")