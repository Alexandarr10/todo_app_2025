while True:
    user_decision = input("Type add, show, edit, exit or complete")
    user_decision = user_decision.strip()

    match user_decision:
        case "add":
            todo = input("Enter a todo: ") + "\n"

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            todos.append(todo)

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

        case "show":
            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            for index, item in enumerate(todos):
                item = item.strip('\n')
                row = f"{index + 1}-{item}"
                print(row)

        case "edit":
            number = int(input("What is the number of the todo to edit: "))
            number = number - 1
            new_todo = input("Edit your todo: ")
            todos[number] = new_todo
        case "complete":
            number = int(input("What is the number of the completed todo: "))
            todos.pop(number - 1)
        case "exit":
            break
        case whatever:
            print("!!!You wrote a wrong command!!!")
print("Bye!")