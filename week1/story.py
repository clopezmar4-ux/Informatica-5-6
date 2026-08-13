def main():
        # planet = input("Planet:")

        # # Separation
        # print("Hello", planet)

        # # Concatenation
        # print("Hello " + planet)

        # # Formatted strings
        # print(f"Hello {planet}")

        # #Ending
        # print("Hello", end=" ")
        # print(planet)
    name = input("What is your name? ").strip().title()
    color = input("Tell me a color: ").strip().lower()
    adjective = input("Give me an adjective: ").strip().lower()
    goal = input("A goal you would like to achive: ").strip().lower()

    print(f"Hello, {name}!", end="\n\n")

    print("This is your story:")

    print(f"A dawn the sky turned {color}, and the air felt {adjective}. I decided today i will finally {goal}.")

    print("....................................................")

    print(f"Hello, {name}!", end="\n\n")

    print("This is your story:")

    print(f"A dawn the sky turned {color}, and the air felt {adjective}. I decided today i will finally {goal}.".upper())



if __name__== "__main__":
        main()
