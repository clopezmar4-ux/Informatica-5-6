def main():
    x = len("hello")
    print(x)

    password = [1, 2, 3, 4, 5, 6, 7, 8]
    xx = ["a", "b", "c", "d"]

    xx.append("e")
    print(len(xx))
    print(password)
    change = input(" ")

    if change == "y":
        password[1]= 4
        password[0] = 2
        password[7] = 1
        password[6] = 9
        password[5] = 10
        password.insert(0,99)
        password.insert(2,42)
        print(password)


    tacos = ["Ojo","tripa","asada","pastor","mixtos"]
    print(tacos.pop(2))
    print(tacos)
    print(tacos.remove("Ojo"))
    print(tacos)

    pets = ["Dog","Cat","Hamster","Fish"]
    pets.append("Bird")
    pets.insert("Bunny")

    numbers = [10, 2, 5, 3, 4, 8, 7]
    print(min(numbers))
    print(max(numbers))
    print(sum(numbers))

    numbers = [1,5,3,7,8,14,21,2]
    numbers.sort(reverse = True)
    print(numbers)

    numbers = [1,5,3,7,8,14,21,2]
    numbers.sort()
    print(numbers)


if __name__=="__main__":
    main()
