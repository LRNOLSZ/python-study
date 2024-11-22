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
print("this is a simple bmi calculator\n")

# def bmi():
#     option = input("please select your option\n"
#           "1. weight in KG, height in M\n"
#           "2. weight in pounds, height in cm")
    #pounds to kg convertor



def option_1():
        weight_pounds = int(input("please state your weight in pounds\n"))
        height_cm = int(input("please state your height in cm\n"))

        #pounds to kg convertor
        weight = round((weight_pounds * 0.453592), 2)
        height = float((height_cm / 100)) 

        #bmi calculator
        def bmi_calculator():
            bmi1 = (weight/(height*height))
            bmi_final = round(bmi1 , 2)
            # print(height , weight)
            # 
            if bmi_final <= 18.5:
                print(f"your bmi is {bmi_final}, you are under weight")    
            elif bmi_final >= 18.6 <= 25:
                print(f"your bmi is {bmi_final}, you are normal weight")
            elif bmi_final >= 25.1 <= 30:
                print(f"your bmi is {bmi_final}, you are over weight")
            elif bmi_final >= 30.1 <= 35:
                print(f"your bmi is {bmi_final}, you are obese")
            else:
                print(f"your bmi is {bmi_final}, you are clinically obese")

        bmi_calculator()
        

def option_2():
        weight = float(input("please state your weight in KG\n"))
        height = float(input("please state your height in M\n"))

        def bmi_calculator():
                bmi1 = (weight/(height*height))
                bmi_final = round(bmi1 , 2)
                # print(height , weight)
                    # 
                if bmi_final <= 18.5:
                    print(f"your bmi is {bmi_final}, you are under weight")    
                elif bmi_final >= 18.6 <= 25:
                    print(f"your bmi is {bmi_final}, you are normal weight")
                elif bmi_final >= 25.1 <= 30:
                    print(f"your bmi is {bmi_final}, you are over weight")
                elif bmi_final >= 30.1 <= 35:
                    print(f"your bmi is {bmi_final}, you are obese")
                else:
                    print(f"your bmi is {bmi_final}, you are clinically obese")

        bmi_calculator()
        
        

option = int(input("please select your option\n"
               "to calculate BMI\n"
               "1. using pounds and cm\n"
               "2. using KG and M\n"))

if option == 1:
    option_1()
elif option == 2:
    option_2()
else:
    print("invalid input")