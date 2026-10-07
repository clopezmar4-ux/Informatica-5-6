def main():



    welcome()
    answer = input("Whats your order: ").lower()
    give_item(answer)

def welcome():
    menu = ["Cheeseburger","Fries","Soda","Ice Cream","Cookie"]
    print("Welcome to Crazy-cook")
    print("Heres the menu:")
    for food in range(len(menu)):
        print(f"{food+1}.{menu[food]}")

def give_item(item):
    emoji = ["🍔", "🍟", "🥤", "🍦", "🍪"]
    if item == "Cheeseburger":
        print(f"{emoji[0]}")
    elif item == "Fries":
        print(f"{emoji[1]}")
    elif item == "Soda":
        print(f"{emoji[2]}")
    elif item == "Ice Cream":
        print(f"{emoji[3]}")
    elif item == "Cookie":
        print(f"{emoji[4]}")


if __name__=="__main__":
    main()
