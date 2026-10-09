def main():



    welcome()
    answer = input("Whats your order: ").lower().strip()
    give_item(answer)

def welcome():
    menu = ["Cheeseburger","Fries","Soda","Ice Cream","Cookie"]
    print("Welcome to Crazy-cook")
    print("Heres the menu:")
    for food in range(len(menu)):
        print(f"{food+1}.{menu[food]}")

def give_item(item):
    emoji = ["🍔", "🍟", "🥤", "🍦", "🍪"]
    if item == "cheeseburger":
        print(emoji[0])
    elif item == "fries":
        print(emoji[1])
    elif item == "soda":
        print(emoji[2])
    elif item == "ice cream":
        print(emoji[3])
    elif item == "cookie":
        print(emoji[4])


if __name__=="__main__":
    main()
