import random

def main():

    person = int(input("If you want heads put 1 but if you want tails put 2: "))

    coin = random.randint(1,2)
    if coin == 1:
        print("Heads")

    elif coin == 2:
        print("Tails")

    if person == coin:
        print("winner")
        
    elif person != coin:
        print("Loser")
    else:
        print("Wrong information")




if __name__=="__main__":
    main()
