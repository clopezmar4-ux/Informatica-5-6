def main():
    w= int(input("Enter width: "))
    p= 2*(w+5)
    a= 5*w
    d= (5**2+w**2)**1/2
    print("O"*w)
    print("O"*w)
    print("O"*w)
    print("O"*w)
    print("O"*w)

    print(" Perimeter:",p)
    print(" Area:",a)
    print(" Diagonal:",d)


if __name__=="__main__":
    main()
