import random

def main():

    print("Super Mathematic Duolingo")

    print("Welcome!, You have three attempts to win.")
    streak = 0
    star = "⭐"


    print(f"What is {number1} + {number2}?")
    guess = input("Your answer: ")

    while streak != 3:
        number1 = random.randint(1,20)
        number2 = random.randint(1,15)
        guess = int()
        add = number1 + number2
            if guess == add:
                print("Correct!, next question")
                print("streak:", star)
            else:
                print("Wrong")
                streak +=1
                print("streak:", star)


if __name__=="__main__":
    main()
