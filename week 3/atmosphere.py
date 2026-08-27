def main():

# Exosphere (700–10,000 km): descent rate = 2000 m/s (near vacuum, free fall)
# Thermosphere (85–700 km): descent rate = 500 m/s (thin air, minimal drag)
# Mesosphere (50–85 km): descent rate = 200 m/s (air thickens, meteors burn here)
# Stratosphere (12–50 km): descent rate = 75 m/s (ozone layer, much denser)
# Troposphere (0–12 km): descent rate = 20 m/s (densest layer, parachute deploys)


    layer = input("Decendent atmosphere layer:").strip().title()
    if layer == "Exosphere":
        print("Your altitude level will be bewteen 700 and 10,000 km")
    elif layer == "Thermosphere":
        print("Your altitude level will be bewteen 85 and 700 km")
    elif layer == "Mesosphere":
        print("Your altitude level will be bewteen 50 and 85 km")
    elif layer == "Stratosphere":
        print("Your altitude level will be bewteen 12 and 50 km")
    elif layer == "Troposphere":
        print("Your altitude level will be bewteen 0 and 12 km")
    else:
        print("Wrong information")
    altitude = float(input("Enter exact altitude: "))

    Ex = float(((altitude - 700)*1000)/2000)
    Th = float(((altitude - 85)*1000)/500)
    Me = float(((altitude - 50)*1000)/200)
    St = float(((altitude - 12)*1000)/75)
    Tr = float(((altitude - 0)*1000)/20)


    if altitude < 10000:
        print(round(Ex+Th+Me+St+Tr,1))
    elif altitude < 700:
        print(round(Th+Me+St+Tr,1))
    elif altitude < 85:
        print(round(Me+St+Tr,1))
    elif altitude < 50:
        print(round(St+Tr,1))
    elif altitude < 12:
        print(round(Tr,1))
    else:
        print("Try again")

if __name__=="__main__":
    main()
