def main():
    print("How many money do you have left?")
    c= float(input("Colombian pesos: "))
    p= float(input("Peruvian pesos: "))
    b= float(input("Brazilian pesos: "))
    u= (c*0.00032)+(p*.30)+(b*.19)
    m= (c*0.0054)+(p*5.07)+(b*3.27)
    print("USD: ",round(u,2))
    print("MXN: ",round(m,2))
if __name__=="__main__":
    main()
