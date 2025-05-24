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
# #                                  BMI                                   #
# print("Welcome to the simple BMI calculator!\n")

# def calculate_bmi(weight, height):
#     # """Calculates BMI and prints the BMI category."""
#     bmi = round(weight / (height ** 2), 2)
#     if bmi <= 18.5:
#         print(f"Your BMI is {bmi}. You are underweight.")
#     elif 18.6 <= bmi <= 25:
#         print(f"Your BMI is {bmi}. You have a normal weight.")
#     elif 25.1 <= bmi <= 30:
#         print(f"Your BMI is {bmi}. You are overweight.")
#     elif 30.1 <= bmi <= 35:
#         print(f"Your BMI is {bmi}. You are obese.")
#     else:
#         print(f"Your BMI is {bmi}. You are clinically obese.")

# def option_1():
#     # """Handles BMI calculation using weight in pounds and height in cm."""
#     try:
#         weight_pounds = float(input("Please state your weight in pounds: "))
#         height_cm = float(input("Please state your height in cm: "))
#         weight_kg = round(weight_pounds * 0.453592, 2)
#         height_m = height_cm / 100
#         calculate_bmi(weight_kg, height_m)
#     except ValueError:
#         print("Invalid input! Please enter numeric values.")

# def option_2():
#     # """Handles BMI calculation using weight in KG and height in M."""
#     try:
#         weight_kg = float(input("Please state your weight in KG: "))
#         height_m = float(input("Please state your height in M: "))
#         calculate_bmi(weight_kg, height_m)
#     except ValueError:
#         print("Invalid input! Please enter numeric values.")

# # Main program flow
# try:
#     option = int(input("Please select your option to calculate BMI:\n"
#                        "1. Using pounds and cm\n"
#                        "2. Using KG and M\n"
#                        "Your choice: "))
#     if option == 1:
#         option_1()
#     elif option == 2:
#         option_2()
#     else:
#         print("Invalid input! Please select option 1 or 2.")
# except ValueError:
#     print("Invalid input! Please enter 1 or 2.")

#               leap_year calculator                #

# # leap year calculator
# def leap_year(year):
#     if year % 4 == 0:
#         # print("sucess div by 4")
#         if year % 100 == 0:
#             # print("sucess div by 100")
#             if year % 400 == 0:
#                 # print("sucess div by 400")
#                 print(f"its a leap year")
#             else:
#                 print(f"its not a leap year")
#         else:
#             print(f"its a leap year")
#     else:
#         print("this is not a leap year")


# #  leap year intro
# # main program flow
# try:
#     user_choice = int(input("this is a simple leap year calculator\n"
#     "please input the year u want to calculate\n"))
#     print(f"the year u inserted is {user_choice}")
#     leap_year(user_choice)
    

# except ValueError:
#     print("input a valid year")



                            # simple pizza ordering      #
# introduction 
# print("this is a simple pizza ordering system\n"
#     "we have three different sizes\n"
#     "small size: 15$\n"
#     "medium size: 20$\n"
#     "large size: 25$\n")





# try:
#     bill = 0
#     user_choice = int(input("what size of pizza would u like to order\n"
#     "1: for small\n"
#     "2: for medium\n"
#     "3: for large size\n"))  
# # small pizza
#     if user_choice == 1:
#         bill += 15
#         pep_choice = int(input("u have selected small\n"
#             f"your current bill is {bill}\n"
#             "do u want to add peppperoni ?\n"
#             "peppperoni cost 2$\n"
#             "1: for yes \n"  "2:for no\n"))
#         if pep_choice == 1:
#             bill += 2
#             print(" thank u for your purchase\n"
#                 f"your current bill is {bill}")
#         else:
#             print(" thank u for your purchase\n"
#                 f"your current bill is {bill}")
            
# # medium pizza
#     if user_choice == 2:
#         bill += 20
#         pep_choice = int(input("u have selected medium\n"
#             f"your current bill is {bill}\n"
#             "do u want to add peppperoni ?\n"
#             "peppperoni cost 3$\n"
#             "1: for yes \n"  "2:for no\n"))
#         if pep_choice == 1:
#             bill += 3
#             print(" thank u for your purchase\n"
#                 f"your current bill is {bill}")
#         else:
#             print(" thank u for your purchase\n"
#                 f"your current bill is {bill}")
# # large pizza
#     if user_choice == 3:
#         bill += 25
#         pep_choice = int(input("u have selected large\n"
#             f"your current bill is {bill}\n"
#             "do u want to add peppperoni ?\n"
#             "peppperoni cost 3$\n"
#             "1: for yes \n"  "2:for no\n"))
#         if pep_choice == 1:
#             bill += 3
#             print(" thank u for your purchase\n"
#                 f"your current bill is {bill}")
#         else:
#             print(" thank u for your purchase\n"
#                 f"your current bill is {bill}")
        
        

# except ValueError: 

#     print("please input the right options")


            # love calculator #

# try:
#   print("welcome to the love calculator")
#   name1 = input("what is your name\n").lower()
#   name2 = input("what is their name\n").lower()

#   combined_name = name1 + name2
  
#   # T
#   t = combined_name.count("t")
#   print(f" t occurs {t} times")
  
#   # R
#   r = combined_name.count("r")
#   print(f" r occurs {r} times")
  
#   # U
#   u = combined_name.count("u")
#   print(f" u occurs {u} times")

#   # E
#   e = combined_name.count("e")
#   print(f" e occurs {e} times")

#   # L
#   l = combined_name.count("l")
#   print(f" l occurs {l} times")

#   # O
#   o = combined_name.count("o")
#   print(f" o occurs {o} times")

#   # V
#   v = combined_name.count("v")
#   print(f" v occurs {v} times")

#   # E
#   e = combined_name.count("e")
#   print(f" e occurs {e} times")

#   true_total = t+r+u+e
#   print(f"true = {true_total}")

#   love_total = l+o+v+e
#   print(f"love = {love_total}")

#   love_score = str(true_total) + str(love_total)
#   love_score_result = int(love_score)
#   print(love_score_result)

#   # range of love 
#   if  love_score_result < 10 and love_score_result > 90 :
#   # if 10 > love_score_result > 90:
#     print(f" you go together like pepsi ")

#   elif 40 < love_score_result < 50:
#   # elif love_score_result > 40 and love_score_result < 50:
#     print(f"you are ok together")
#   else:
#     print(f"you are there")

# except ValueError:
#   print("invalid input")
      

try:

  
  welcome = input("welcome to the guessing game\n"
        "Are you ready to begin\n"
        "Yes or No\n").lower()
  
  
  
        # starting point
  if welcome == "yes":  
    # congratulations function
    def congratulations(user_name):
      return f"congratulations {user_name} u progress to the next level"

    user_name = input("Before we begin what is your name\n")
    cong_message = congratulations(user_name)

  #ending function
    def ending(user_name):
      return f" sorry {user_name} this is the end of the line for u"
    ending_message = ending(user_name)

  #wrong function
    def wrong_input():
      return f"incorrect input"    
        # Greeting
    print(f"welcome to the game {user_name} ")
    #question 1
    left_right = input("Left or Right\n").lower()
    if left_right == "left":
      print(cong_message)
      #Question 2
      swim_wait = input("now do u want to swim or wait\n").lower()
      if swim_wait == "swim":
        print(cong_message)
        # question 3
        door = input("now choose which door, red or blue\n").lower()
        if door == "red":
          print(cong_message)
          #Question 4
          born_year = str(input(f"Which year were you born {user_name}\n"))
          if 2001 <= born_year <= 2025:
            print(cong_message)
            #question 5
            game_ending = input(f"do u think this is the ending {user_name}\n"
            "Yes or no\n").lower()
            if game_ending == "no":
              print(cong_message)
              print(f" Stay in touch for part 2")
            elif game_ending == "yes":
              print(ending_message)
              print("Sorry, this was a trick question haha u loose")
            else:
              wrong_input()
          elif born_year <= 2000 or born_year >= 2026:
            print(ending_message)
          else:
            wrong_input()
        elif door == "blue":
          print(ending_message)
        else:
          wrong_input()
      elif swim_wait == "wait":
        print(ending_message)
      else:
        wrong_input()
    elif left_right == "right":
        print(ending_message)
    else:
      wrong_input()

  elif welcome == "no":
    print("that was unfortunate , see u another time")

  else:
    print("incorrect input")
  

except ValueError:
  print("invalid input")