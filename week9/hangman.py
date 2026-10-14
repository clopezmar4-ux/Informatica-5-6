
import random #Import the random library
def main(): # Define the main function
# Create a TXT file name "words"
#random.txt
# Write possible words in the file
#random.txt
    start_game("random.txt") # called the function

def start_game(file): # Define a function name start_game(file)
    with open("random.txt") as words_file:# Read the file
        content = words_file.read().splitlines()
        #print(random.choice(content)) to check that you doing it right
    pam = random.choice(content)#create a variable and print a random choice of the file
    x = ["_"] * len(pam)# make a variable= "_" * len(file)
    print(" ".join(x))#print the variable
    while True:# make a while loop
        guess = input("Guess a letter: ").strip()
        if len(guess) == 1:# Make an if statement for the letter the user enter only one letter
         break
        else:# Make a else to say if is not just one letter
            print("invalid option")
    for i in pam:
        if guess == i:
            print(guess)




# if the letter is in the word print the letter in the place that belongs to it
#take one of the attempts if they got it wrong
# if they put more than one letter at the time tell them that they are wrong
# if they run out of chances finish the program
# print a welcome to the game
#give them a happy face if they get the word right
# give them a sad face if they get it wrong
# Make a variable of (input) for the answer of the user
# Make a variable with the attempts they have
#print how many they have left
# Make a for loop


if __name__=="__main__":
    main()
