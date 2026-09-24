def main():
    character = ["Mario","Luigi","Daysi","Yoshi","Toad","Princess Peach","Bowser"]

    for receiver in character :
        if receiver != "Princess Peach":
            print(f"""
    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
       Dear {receiver},

       You are cordially invited to a ball at
       Peach's Castle this evening, 7:00 PM.

       Sincerely,
       {character[5]}
    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
""")

if __name__=="__main__":
    main()
