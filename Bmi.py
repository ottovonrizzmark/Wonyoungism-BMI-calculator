weight = float(input("Enter your weight in kg."))
height = float(input("Enter your height in meters."))
height_squared = height ** 2
BMI = round(weight / height_squared, 2)

print(f"Your BMI is {BMI}.")

if BMI < 18.5:
    print("NOT YOU BEING IN YOUR WOONYOUNG ERA")
elif 18.5 <= BMI <= 24.9:
    print("Chile... you’re doing fine. Keep slaying.")
else:
    print("FATTY?! Time to hit the gym!")



    
