import random

def main():

    print("Super Mathematic Duolingo")

    print("Welcome!, You have three attempts to win.")
    streak = 0
    star = "⭐"

    while streak != 3:

        number1 = random.randint(1,20)
        number2 = random.randint(1,15)
        guess = float()
        add = number1 + number2
        multy = number1 * number2
        sub = number1 - number2
        div = round(number1 / number2,2)
        operation = ("+","*","-","/")
        op = random.choice(operation)

        print(f"What is {number1} {op} {number2}?")
        guess = round(float(input("Your answer: ")),2)

        if guess == add:
            streak += 1
            if streak == 1:
                print("streak:", star)
                print("Correct!, next question")
            elif streak == 2:
                print("streak:", star + star)
                print("Correct!, next question")
            else:
                print("Streak:",star + star + star)
                print("You are a genius!, see you next time")

        elif guess == multy:
            treak += 1
            if streak == 1:
                print("streak:", star)
                print("Correct!, next question")
            elif streak == 2:
                print("streak:", star + star)
                print("Correct!, next question")
            else:
                print("Streak:",star + star + star)
                print("You are a genius!, see you next time")
        elif guess == sub:
            streak += 1
            if streak == 1:
                print("streak:", star)
                print("Correct!, next question")
            elif streak == 2:
                print("streak:", star + star)
                print("Correct!, next question")
            else:
                print("Streak:",star + star + star)
                print("You are a genius!, see you next time")
        elif guess == div:
            streak += 1
            if streak == 1:
                print("streak:", star)
                print("Correct!, next question")
            elif streak == 2:
                print("streak:", star + star)
                print("Correct!, next question")
            else:
                print("Streak:",star + star + star)
                print("You are a genius!, see you next time")

        else:
            if streak == 3:
                break


if __name__=="__main__":
    main()
