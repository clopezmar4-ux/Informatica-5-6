def main():
    #this is finite loop
    phrase = ""
    followup = ""

    while phrase != "Yes!":
        phrase = input("Are we there yet? ").title().strip()
        if phrase == "Yes":
            followup = input("Really? ").title().strip()
        if followup == "Yes":
            break

    print("Finally!")
    # until while is false it will print whats inside the print


if __name__=="__main__":
    main()
