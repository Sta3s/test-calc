from functions import calculate_calories_burned

print("Welcome to the Calories Burned Calculator!")
activity = input("Enter the activity (e.g., running, cycling, swimming): ")
duration = float(input("Enter the duration of activity in minutes: "))
weight = float(input("Enter your weight in kilograms: "))
calories_burned = calculate_calories_burned(activity, duration, weight)

if isinstance(calories_burned, str):
    print(calories_burned)
else:
    print("You burned calories.", calories_burned)

# Happy-Path
# 1. It is known that we learn the number of calories burned as a result of the product of time, type of activity and our weight, 
#    If we introduce swimming, 20 minutes and our weight is 60 kilograms, then we have burned 140 calories
    
# Use-Case
# 1. It is known that we learn the number of calories burned as a result of the product of time, type of activity and our weight, 
#    If we enter swimming, 240 minutes and our weight is 60 kilograms, then we have burned 1680 calories
# 2. It is known that we know the number of calories burned as a result of the product of time, type of activity and our weight, 
#    If we enter running, 0 minutes and our weight is 60 kilograms, then we have burned 0 calories
# 3. It is known that we know the number of calories burned as a result of the product of time, type of activity and our weight, 
#    If we enter running, 1 minute and our weight is 130 kilograms, then we have burned 21.6666666666666664 calories
# 4. It is known that we know the number of calories burned as a result of the product of time, type of activity and our weight, 
#    If we introduce cycling, 0.5 minutes and our weight is 50 kilograms, then we have burned 3.333333333333333335 calories
# 5. It is known that we learn the number of calories burned as a result of the product of time, type of activity and our weight, 
#    If we enter cycling, 80 minutes and our weight is 70.6 kilograms, then we have burned 753.066666666666666 calories
    

# Edge-Case
# 1. It is known that we learn the number of calories burned as a result of the product of time, type of activity and our weight, 
#    If we introduce swimming, -2 minutes and our weight is 60 kilograms, then we have burned -14.0 calories
# 2. It is known that we know the number of calories burned as a result of the product of time, type of activity and our weight, 
#    If we enter running, 0 minutes and our weight is 0 kilograms, then we have burned 0 calories
# 3. It is known that we know the number of calories burned as a result of the product of time, type of activity and our weight, 
#    If we enter a box, it gives an error
# 4. It is known that we know the number of calories burned as a result of the product of time, type of activity and our weight, 
#    If we enter cycling, minute, it gives an error
# 5. It is known that we know the number of calories burned as a result of the product of time, type of activity and our weight, 
#    If we introduce cycling, 9999999 minutes and our weight 9999999999999 kilogram, then we have burned 1.3333331999998667E+19 calories