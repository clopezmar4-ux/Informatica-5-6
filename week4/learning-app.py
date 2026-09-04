import random

def main():

    print("Super Mathematic Duolingo")

    print("Welcome!, You have three attempts to win.")
    streak = 0
    star = "⭐"

    while streak != 3:

        number1 = random.randint(1,20)
        number2 = random.randint(1,15)
        guess = int()
        add = number1 + number2

        print(f"What is {number1} + {number2}?")
        guess = input("Your answer: ")

        if guess == add:
            streak += 1
            print("Correct!, next question")
            if streak == 1:
                print("streak:", star)
            elif streak == 2:
                print("streak:", star, star)
            else:
                print("Streak:",star,star,star)
        elif guess != add:
            print("Incorrect")

        else:
            streak == 3
            break


if __name__=="__main__":
    main()
