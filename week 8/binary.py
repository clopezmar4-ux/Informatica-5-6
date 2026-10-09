def main():
    print("Welcome to Binary to Decimal Converter!")
    print("[In this program you will recibe the decimal answer that belongs to your binary number.]")
    valid = ["0","1"]
    while True:
        find = input("Enter a binary number: ")
        valid_ = 0
        for v_bit in find:
            if v_bit in valid:
                valid_ +=1
        if valid_ == len(find):
            break
        else:
            print("Invalid")
    binary_to_decimal(find)
def binary_to_decimal(binary):
    decimal = 0
    list = []
    for bit in binary:
        list.append(binary[bit])
        list.reverse()
    for bit in range(len(list)):
        if bit == '1':
            decimal += 2**(bit+1)
    print(int(decimal))
if __name__=="__main__":
    main()

