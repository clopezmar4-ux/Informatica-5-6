def main():

    transistors = 17800000000
    year = int(input("Years in the future: "))
    transistors *= 2**(year/2)
    print(f"These are the numbers of transistors in {year} years: {transistors}")

if __name__=="__main__":
    main()
