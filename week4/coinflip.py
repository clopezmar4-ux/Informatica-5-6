import random

def main():


    coin = ["heads","tails"]
    coin = random.choice(coin)
    attempts = 3

    while attempts > 0:
        person = input("You want heads or tails: ").strip().lower()

        print("The coin landed on",coin)
        if person == coin:
            print("winner")
            break
        elif person != coin:
            print("Loser")
            attempts -= 1
            print("attempts left:", attempts)
        else:
            if attempts == 0:
                print("You dont have more oportunities")




if __name__=="__main__":
    main()
