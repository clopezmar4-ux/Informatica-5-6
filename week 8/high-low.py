def main():
    def highest(a,b):
        if a>b:
            highest_num = a
            print(f"The highest number entered is {highest_num}")
        else:
            highest_num = b
            print(f"The highest number entered is {highest_num}")

    highest(8,2)
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter a second number: "))

    highest(num1,num2)
    print()

    def lowest(a,b,c):
            if a<b and a<c:
                lowest_num = a
                print(f"The lowest number entered is {lowest_num}")
            elif b<a and b<c:
                lowest_num = b
                print(f"The lowest number entered is {lowest_num}")
            else:
                 lowest_num = c
                 print(f"The lowest number entered is {lowest_num}")

    lowest(8,2,9)
    num3 = int(input("Enter a number: "))
    num4 = int(input("Enter a second number: "))
    num5 = int(input("Enter a third number: "))

    lowest(num3,num4,num5)





if __name__=="__main__":
    main()
