def main():

    #Absolute Value Calculator
    integer = int(input("Enter an integer: "))
    negative = integer * -1
    if integer < 0:
        print(negative)
    elif integer > 0:
        print(integer)
    print("Thank you")

    #Input Calculator
    print("Give me two numbers and an operation")
    number1 = float(input("Number 1: "))
    number2 = float(input("Number 2: "))
    operation = input("Operation: ")
    add = number1+number2
    multiply = number1*number2
    subtract = number1-number2


    if operation == add:
        print(add)
    elif operation == multiply:
        print(multiply)
    elif operation == subtract:
        print(subtract)
    else:
        print()

    #String Calculator
    operation = float(input("Write an arithmethic expression: "))
    part = operation.split()
    


if __name__=="__main__":
    main()
