#simple even or od number code
print("this is an oddd or even number checker\n")


def checker():   
    number = int(input("please give your number\n"))
    if number % 2 == 0:
        print(f"{number} is an even number")
    else:
        print(f"{number} is an odd number")

checker()