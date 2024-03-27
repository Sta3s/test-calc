from functions import calculate_bmi, interpret_bmi

print("Welcome to the BMI Calculator!")
weight_kg = float(input("Enter your weight in kilograms: "))
height_m = float(input("Enter your height in meters: "))
bmi = calculate_bmi(weight_kg, height_m)
interpretation = interpret_bmi(bmi)
print("Your BMI is {:.2f}".format(bmi))
print("Interpretation: ", interpretation)

# Happy-Path
# 1. It is known that BMI is equal to the division of weight (kg) by height squared (m), if we enter a weight of 60 kg and a height of 1.75 m, then our BMI is 19.59

# Use-Case
# 1. It is known that BMI is equal to dividing weight (kg) by height squared (m), if we enter weight 0 kg and height 1.50 m, then our BMI is 0.00 
# 2. It is known that BMI is equal to the division of weight (kg) by height squared (m), if we enter a weight of 50 kg and a height of 0 m, then an error is generated
# 3. It is known that BMI is equal to dividing weight (kg) by height squared (m), if we enter weight 50 kg and height 100 m, then our BMI is 0.01
# 4. It is known that BMI is equal to dividing weight (kg) by height squared (m), if we enter weight 1000 kg and height 0.25 m, then our BMI is 16000.00
# 5. It is known that BMI is equal to dividing weight (kg) by height squared (m), if we enter weight 0.1 kg and height 0.5 m, then our BMI is 0.40

# Edge-Case
# 1. It is known that BMI is equal to dividing weight (kg) by height squared (m), if we enter weight -1 kg and height 10 m, then our BMI is -0.01
# 2. It is known that BMI is equal to dividing weight (kg) by height squared (m), if we enter weight 9999999999 kg and height 1 m, then our BMI is 9999999999.00
# 3. It is known that BMI is equal to dividing weight (kg) by height squared (m), if we enter weight 50.2123432423 kg and height -100.44 m, then our BMI is 0.00
# 4. It is known that BMI is equal to the division of weight (kg) by height squared (m), if we enter weight Weight, then an error is generated
# 5. It is known that BMI is equal to dividing weight (kg) by height squared (m), if we enter a weight of 1.0.1 kg, then an error is generated