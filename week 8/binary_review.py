def main():
    print("welcome!")
    print("purpose")

    valid_bits = ["0","1"]
    while True:
        user_binary_num = input("Enter a binary number: ")
        valid_chars = 0
        for user_bit in user_binary_num:
            if user_bit in valid_bits:
                valid_chars += 1
        if valid_chars == len(user_binary_num):
            break
        else:
            print("Invalid number")
    binary_to_decimal(user_binary_num)

def binary_to_decimal(binary_num):
    decimal_num = 0
    for bit in binary_num:
        decimal_num = (decimal_num *2) + int(bit)
    print(decimal_num)
if __name__=="__main__":
    main()
