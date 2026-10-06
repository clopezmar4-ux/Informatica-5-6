def main():
    # TO-DO: Define day1, day2, and day3 lists here
    day1 = [26,26,26,25,24,23,21,21,20]
    day2 =[19,19,18,18,17,17,16,16,18,20,22,24,25,26,27,27,27,27,26,25,23,22,21,20,]
    day3 =[19,18,18,17,16,16,16,16,17,20,22,23,25,26,26,27]
    # TO-DO: Print daily headers and call max_temperature / min_temperature
    print("Today")
    max_temperature(day1)
    min_temperature(day1)
    print()

    print("Tomorrow")
    max_temperature(day2)
    min_temperature(day2)
    print()

    print("Day after tomorrow")
    max_temperature(day3)
    min_temperature(day3)
def max_temperature(temperatures):
    # TO-DO: Find and print the highest temperature in the list
    highest_temp = temperatures[0]
    for hour in temperatures:
        if hour > highest_temp:
            highest_temp = hour
    print(f"High {highest_temp}°")

def min_temperature(temperatures):
    # TO-DO: Find and print the lowest temperature in the list
    lowest_temp = temperatures[0]
    for hour in temperatures:
        if hour < lowest_temp:
            lowest_temp = hour
    print(f"Low {lowest_temp}°")
if __name__=="__main__":
    main()
