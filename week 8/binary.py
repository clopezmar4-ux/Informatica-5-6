def main():
    print("Welcome to Binary to Decimal Converter!")
    print("[In this program you will recibe the decimal answer that belongs to your binary number.]")
    find = list(input("Enter a binary number: "))
    print("Decimal number: ")
    binary_to_decimal(find)
def binary_to_decimal(binary):
    decimal = 0
    list = []
    for i in binary:
        list.append(int(binary[i]))
        list.reverse()
    for digit in range(len(list)):
        if digit == '1':
            decimal += 2**(digit+1)

if __name__=="__main__":
    main()

