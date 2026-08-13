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
    name = input("What is your name? ")
    color = input("Tell me a color: ")
    adjective = input("Give me an adjective: ")
    goal = input("A goal you would like to achive: ")

    print(f"Hello, {name}!", end="\n\n")

    print("This is your story:")

    print(f"A dawn the sky turned {color}, and the air felt {adjective}. I decided today i will finally {goal}.")

if __name__== "__main__":
        main()
