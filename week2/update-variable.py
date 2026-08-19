def main():
    # Augmeted assignment operator

    score = 10
    score2 = score + 10 #Normal thougth
    score += 10 # easy way so we cannot need to write another variable
    print(score)

    # Substraction assignment operator

    # x = x - y # Normal way

    # x -= y # easy way so we cannot need to write another variable

    grade = 100
    grade -= 15
    print(grade)

    #Multiplication assigment operator

    balance = 10 # Variable
    #score = balance * 4 # Long way
    balance *= 4 # shortcut
    print(balance)
    # — mdash = alt + 0151 in the right side of the keyboard

    # Division assignment operator

    x = 10
    x /= 5
    print(int(x)) #if we use int then it will be an integer again instead of a float

    # Modulus assignment operator

    #Modulus = remain

    a = 10
    b = 4

    a %= b
    print(a)

if __name__=="__main__":
    main()
