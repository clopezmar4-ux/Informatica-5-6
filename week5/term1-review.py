from datetime import datetime
def main():


    day = datetime.now().weekday()
    days = ["Monday","Tuesday","Wednasday","Thursday","Friday","Saturday","Sunday"]
    print(days[day])

    if day < 4:
        print("It's a weekday")
        remaining =  5 - day
        print(remaining, "days until the weekend")
    elif day == 4:
        print("It's Friday")
        print("Just a day left until the weekend")
    else:
        print("It's the weekend")
    months = ["January","February","March","April","May","June","July","August","September","October","November","December"]
    seasons = ["Winter", "Spring","Summer","Autumn"]

    print("These are the summer months:")
    print(months[5])
    print(months[6])
    print(months[7])

    month = datetime.now().month
    print("It is", months[month-1])

    if month <= 2 or month == 2:
        season = 0
    elif month <= 5:
        season = 1
    elif month <= 8:
        season = 2
    else:
        season = 3
        
    print("It is", seasons[season])


if __name__=="__main__":
    main()
