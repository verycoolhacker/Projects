import math

while True:

    action = input("Hello user please type the following symbol of your choice:+, -, /, *"   )
    number1 = int(input("Please select first number: "))
    number2 = int(input("Now enter your second number: "))

    if action == "+":
        print(number1 + number2)
    elif action == "-":
        print(number1 - number2)
    elif action == "/":
        print(number1 / number2)
    elif action == "*":
        print(number1 * number2)


    question = input("User would you like to close the program now?:Yes, No  ")

    if question == "Yes":
        print("Goodbye!")
        break
    elif question =="No":
        print("Restarting..")
    elif question =="yes":
        print("Goodbye!")
        break
    elif question =="no":
        print("Restarting..")
    else:
        print("error unknown response restarting!")