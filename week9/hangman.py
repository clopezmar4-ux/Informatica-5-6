# Create a TXT file name "words"
#random.txt
# Write possible words in the file
#random.txt
import random #Import the random library
def main(): # Define the main function

    start_game("random.txt") # called the function

def start_game(file): # Define a function name start_game(file)
    print("Welcome to Hangman!")# print a welcome to the game
    attempts = 10# Make a variable with the attempts they have
    with open("random.txt") as words_file:# Read the file
        word = words_file.read().splitlines()# convert the file ino a list
        #print(random.choice(content)) to check that you doing it right
    pam = random.choice(word).lower()#create a variable and print a random choice of the file
    x = ["_"] * len(pam)# make a variable= "_" * len(file)
    incorrect_letters = [] #make an incorrect list
    while attempts > 0: # make a while with the attempts
        print("Current word:", " ".join(x))#print the variable

        while True:# make a while loop
            guess = input("Guess a letter: ").strip()# Make a variable of (input) for the answer of the user
            if len(guess) == 1:# Make an if statement for the letter the user enter only one letter
                break # break the program
            else:# Make a else to say that its not a valid option
                print("invalid option")
        if guess in pam and guess not in x:
            for i in range(len(pam)):# Make a for loop
                if pam[i] == guess:
                    x[i] = guess # if the letter is in the word print the letter in the place that belongs to it
            print("Great guess!")
        elif guess in x:
            attempts -= 1#take one of the attempts if they got it wrong
            print("You already guessed that letter! Attempts left:", str(attempts))# if they put more than one letter at the time tell them that they are wrong
        else:
            attempts -= 1
            print("Wrong guess! Attempts left:", str(attempts))#print how many they have left
            if guess not in incorrect_letters:
                incorrect_letters.append(guess)
            print(f"Incorrect letters: {" ".join(incorrect_letters)}")
        if "_" not in x:
            print("Congratulations! 🥳 You guessed the word:", pam)#give them a happy face if they get the word right
            break

    if attempts == 0 and "_" in x:
        print("No attempts left 💀 The word was:", pam)# if they run out of chances finish the program

if __name__=="__main__":
    main()
