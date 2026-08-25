def main():

    print("periwinkle")
    rating = float(input("Rate our service from 0 to 5: "))
    if rating > 5:
        print("I love it but choose a smaller number")
    elif rating > 4.5:
        print("Perfection")
    elif rating > 4:
        print("Excellent")
    elif rating > 3:
        print("Good")
    elif rating > 2:
        print("fair")
    else:
        print("Poor")
    print("Thank you for being honest!")


if __name__=="__main__":
    main()
