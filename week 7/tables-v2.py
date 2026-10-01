def main():
    valid_nums = []

    for i in range(1,11):
        valid_nums.append(str(i))

    print("Welcome to the time tables quiz!")
    while True:
        try:
            times_table = int(input("Enter a times table that you would like to be tested on: "))
            break
        except ValueError:
            print("You must enter a number")

    if times_table in valid_nums:
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
