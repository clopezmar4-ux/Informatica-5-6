def main():
    #fruits = ["apple", "banana", "cherry", "aguacate"]
    #print("pineapple" not in fruits)
    #fruits = "apple"
    #print("b" not in fruits)


    tasks = []
    list2 = []
    while True:
        print(f"Tasks to do: {len(tasks)}")
        print(tasks)
        new_task =input("Enter task: ").capitalize().strip()

        if new_task == "Exit":
            break
        elif new_task not in tasks:
            tasks.append(new_task)
        elif new_task in tasks:
            tasks.remove(new_task)
            print("Task remove from the list.")
            list2.append(new_task)

        if new_task in list2:
            print(f"Task removed: {list2}")


if __name__=="__main__":
    main()
