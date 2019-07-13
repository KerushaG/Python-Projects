#Introduction to Programming, Task 24.3
#Kerusha Govender 4 May 2019
#A program that takes in the users choice of two numbers and performs the calculation chosen by the user through a menu of options.

#I definited the different operations and the menu.
def addNum(num1, num2):
    x = num1 + num2
    #return x
    print(x)

def subtractNum(num1, num2):
    x = num1 - num2
    #return x
    print(x)

def multiplyNum(num1, num2):
    x = num1 * num2
    #return x
    print(x)

def divideNum(num1, num2):
    x = num1 / num2
    #return x
    print(x)

def menu():
    print("Option 1 - add")
    print("Option 2 - subtract")
    print("Option 3 - multiply")
    print("Option 4 - divide")
    print("Option 5 - exit")

num1 = 0
num2 = 0
#Here I made a separate function that asks the user for their choice of operation, if they don't pick the right one, it keeps asking. Once they pick a valid choice,
#I use if statements to call on the relevant functions, with the users number choices to perform and give the answer.
#Not sure about the difference between return and print here, because return gave nothing.
def calculator():
    option = 0
    while option < 1 or option > 5:
        option = int(input("Choose the operation you would like to use: (Type 1-5) "))
        if option == 5:
            break
        elif option >= 1 and option <= 4:
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            if option == 1:
                addNum(num1, num2)
            elif option == 2:
                subtractNum(num1, num2)
            elif option == 3:
                multiplyNum(num1, num2)
            elif option == 4:
                divideNum(num1, num2)
#After the operation is performed, I created a loop function, that asks the user if they want to use the calculator again.
def calculatorloop():
    while True:
        Again = input("Would you like to use the calculator again? (yes or no) ")
        again = Again.lower()
        if again == 'yes':
            calculator()
        else:
            break

def main():
    menu()
    calculator()
    calculatorloop()
    
####################################################
#I put the 3 main functions under a new function called main and called only main

main()    
