def main():

    number = [1,2,3,4,5,6,7,8,9,10]
    while True:
            user = input("Do you want a multiplication table? ").strip().lower()
            if user == "no":
                 print("Thanks for aswering")
                 break
            if user == "yes":
                table = int(input("Enter a number (1-10): "))
                print(f"Here is the {table} times table")
                if table in number:
                    for num in range(len(number)):
                        times = table * (num+1)
                        print(f"{num+1} times {table} is {times}")
                followup= input("Do you want another one? if not write exit: ").strip().lower()
            if followup == "exit":
                 print("Thanks for aswering")
                 break








if __name__=="__main__":
    main()
