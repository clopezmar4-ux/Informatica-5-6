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
    
    if operation == "add":
        print(number1+number2)
    elif operation == "multiply":
        print(number1*number2)
    elif operation == "subtract":
        print(number1-number2)
    else:
        print()

    #String Calculator
    operation = float(input("Write an arithmethic expression: "))
    part = operation.split()



if __name__=="__main__":
    main()
