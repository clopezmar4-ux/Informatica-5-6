#Import the random library
import random
# Define the main function
def main():
# Create a TXT file name "words"
#random.txt
# Write possible words in the file
#random.txt
    start_game("random.txt")
# Define a function name start_game(file)
def start_game(file):
# Read the file
#print a random choice of the file
    with open("random.txt") as words_file:
        content = words_file.read().splitlines()
        print(random.choice(content))
# Make a variable of (input) for the answer of the user
# Make a variable with the attempts they have
#print how many they have left
# Make a for loop
# make a variable= "_" * len(file)
#print the variable
# Make an if statement for the letter the user enter if is in the word or not
# Make a elif to say if the letter is not in the word
# if the letter is in the word print the letter in the place that belongs to it
#take one of the attempts if they got it wrong
# if they put more than one letter at the time tell them that they are wrong
# if they run out of chances finish the program
# print a welcome to the game
#give them a happy face if they get the word right
# give them a sad face if they get it wrong
#
#

if __name__=="__main__":
    main()
