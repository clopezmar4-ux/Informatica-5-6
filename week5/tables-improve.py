def main():

    while True:
        times_table = input("Enter a number: ").lower().strip()

        if times_table == "exit":
            break
        else:

            max_value = int(input("Enter maximun value for the times table: "))
            print(f"Here is the {times_table} times table")

            for x in range(1,max_value + 1):
                answer = x * int(times_table)
                print(f"{x} times {times_table} is {answer}")

if __name__=="__main__":
    main()
