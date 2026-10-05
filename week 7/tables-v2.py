def main():

    print("Welcome to the time tables quiz!")
    while True:
        try:
            times_table = int(input("Enter a times table that you would like to be tested on (1-10): "))
            if times_table >= 1 and times_table <=10:
                break
            else:
                print("Write a positive number")
        except ValueError:
            print("You must enter a positive number")

    if times_table >= 1 and times_table <= 10:
        while True:
            try:
                max_value = int(input("Enter maximun value for the times table: "))
                print(f"You will be tested in the {times_table} times table and you can only have three incorrect answers")
                break
            except ValueError:
                print("You must enter a number")

        for x in range(1,max_value + 1):
            answer = x * int(times_table)
            while True:
                try:
                    user_answer = int(input(f"{times_table}x{x}= "))
                    if user_answer==answer:
                        print("Correct")
                    elif user_answer != answer:
                        print ("Incorrect")
                    break
                except ValueError:
                    print("You must enter a number.")



if __name__=="__main__":
    main()
