import time
def main():
   #Water goal

   cups_goal = 8
   cups_taken = 0
   drink = int()

   print("   Water tracker    ")
   print(f"Your goal for today is: {cups_goal}")

   while cups_taken < cups_goal:
      drink = int(input("How many cups do you take already?"))
      cups_taken += drink
      cups_left = cups_goal - cups_taken

      if drink <= cups_goal:
         print(f"You almost got it!, you have drunk {drink} cups and you have {cups_left} more left to complete the goal")
         time.sleep(120)

         if cups_left > 0:
            print("Its time for another cup of water")
            time.sleep(1)

         elif cups_left == 0:
             print(f"congratulation you hit your goal of {cups_goal} cups of water today!!")
             print("See you tomorrow")

      else:
         if cups_goal > 8:
            print("You reach your goal and drunk more than we expected")
            break

if __name__=="__main__":
    main()
