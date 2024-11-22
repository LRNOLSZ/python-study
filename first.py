#simple even or od number code
# print("this is an oddd or even number checker\n")

# def checker():   
#     number = int(input("please give your number\n"))
#     if number % 2 == 0:
#         print(f"{number} is an even number")
#     else:
#         print(f"{number} is an odd number")

# checker()
#############################

#                                  BMI                                   #
#                                  BMI                                   #
print("Welcome to the simple BMI calculator!\n")

def calculate_bmi(weight, height):
    # """Calculates BMI and prints the BMI category."""
    bmi = round(weight / (height ** 2), 2)
    if bmi <= 18.5:
        print(f"Your BMI is {bmi}. You are underweight.")
    elif 18.6 <= bmi <= 25:
        print(f"Your BMI is {bmi}. You have a normal weight.")
    elif 25.1 <= bmi <= 30:
        print(f"Your BMI is {bmi}. You are overweight.")
    elif 30.1 <= bmi <= 35:
        print(f"Your BMI is {bmi}. You are obese.")
    else:
        print(f"Your BMI is {bmi}. You are clinically obese.")

def option_1():
    # """Handles BMI calculation using weight in pounds and height in cm."""
    try:
        weight_pounds = float(input("Please state your weight in pounds: "))
        height_cm = float(input("Please state your height in cm: "))
        weight_kg = round(weight_pounds * 0.453592, 2)
        height_m = height_cm / 100
        calculate_bmi(weight_kg, height_m)
    except ValueError:
        print("Invalid input! Please enter numeric values.")

def option_2():
    # """Handles BMI calculation using weight in KG and height in M."""
    try:
        weight_kg = float(input("Please state your weight in KG: "))
        height_m = float(input("Please state your height in M: "))
        calculate_bmi(weight_kg, height_m)
    except ValueError:
        print("Invalid input! Please enter numeric values.")

# Main program flow
try:
    option = int(input("Please select your option to calculate BMI:\n"
                       "1. Using pounds and cm\n"
                       "2. Using KG and M\n"
                       "Your choice: "))
    if option == 1:
        option_1()
    elif option == 2:
        option_2()
    else:
        print("Invalid input! Please select option 1 or 2.")
except ValueError:
    print("Invalid input! Please enter 1 or 2.")
