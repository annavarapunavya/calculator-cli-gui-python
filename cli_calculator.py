#Importing functions from utility file
from utils import add, subtract, multiply, divide

while(True):
    #Menu to select the Operation   
    print("Calculator Menu")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5.Exit")


    choice = input("Enter your choice (1-4): ")

    #Exit option
    if choice == "5":
        print("Exiting calculator...")
        break

    #Taking input numbers from users
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

    except ValueError:
        print("Invalid input! Please enter numbers.")
        exit()

    #Operations
    if choice == "1":
        print("Result:", add(num1, num2))

    elif choice == "2":
        print("Result:", subtract(num1, num2))

    elif choice == "3":
        print("Result:", multiply(num1, num2))

    elif choice == "4":
        print("Result:", divide(num1, num2))

    else:
        print("Invalid choice")
