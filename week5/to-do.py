def main():
    tasks = [] #Empty list
    #tasks = [""] 1 element
    # command = "" we are not gonna used if we use true

    while True: # its the same as command != "exit"
        print(f"Tasks to do: {len(tasks)}")
        print(tasks)
        command = input("What do you want to do? (add, complete, exit): ").lower()
        if command == "add":
            new_task = input("Enter new task: ")
            tasks.append(new_task)
        elif command == "complete":
                remove_task = input("Which task do you complete? ")
                if remove_task == "all":
                     tasks.clear()
                elif remove_task == tasks:
                     tasks.pop(remove_task)
        elif command == "exit":
             break





if __name__=="__main__":
    main()
