todo_list = []

while True:
    print("_____ To Do List _____")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Remove a task")
    print("4. Update a task")
    print("5. Exit  ")
    choice = input("Enter your choice: ")

    if choice == "1":
        print("1. Add a task")
        f_task = (input("Enter a task you want to add: "))
        todo_list.append(f_task)
        print(todo_list)
    elif choice == "2":
        print("2. View tasks")
        print(todo_list)

    elif choice == "3":
          print("3. Remove a task")
          f_task= (input("Enter a task you want to remove: "))
          todo_list.remove(f_task)
          print(todo_list)

    elif choice == "4":
        print("4. Update a task")
        f_task = (input("Enter a task you want to update: "))
        todo_list.append(f_task)
        print(todo_list)

    elif choice == "5":
        print("5. Exit  ")

    break