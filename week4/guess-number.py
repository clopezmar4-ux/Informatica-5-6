import random

def main():
    easy = random.randint(1,20)
    medium = random.randint(1,100)
    harder = random.randint(1,1000)
    number = int()
    attempt = 3

    user = input("Hello! What is your name? ").title()
    level = input("which difficulty level you want to play, easy, medium or harder? ")
    if level == "easy":
        print(f"Well, {user}, I am thinking of a number between 1 and 20")
        while attempt > 0:
            while number != easy:
                number = int(input("Take a guess: "))
                if number > easy:
                    print("Your guess is too high")
                    attempt -= 1
                    print("Attempts left:", attempt)
                elif number < easy:
                    print("Your guess is too low")
                    attempt -= 1
                    print("Attempts left:", attempt)
                elif number == easy:
                    print(f"Good job, {user}! You guessed my number!")
                else:
                    attempt == 0
                    print("Sorry you lose")
                    break

    elif level == medium:
        print(f"Well, {user}, I am thinking of a number between 1 and 100")
        while number != medium:
            number = int(input("Take a guess: "))
            if number > medium:
                print("Your guess is too high")
            elif number < medium:
                print("Your guess is too low")
            else:
                print(f"Good job, {user}! You guessed my number!")
                break
    elif level == harder:
        print(f"Well, {user}, I am thinking of a number between 1 and 1000")
        while number != harder:
            number = int(input("Take a guess: "))
            if number > harder:
                print("Your guess is too high")
            elif number < harder:
                print("Your guess is too low")
            else:
                print(f"Good job, {user}! You guessed my number!")
                break



if __name__=="__main__":
    main()
