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

            with open('todos.txt', 'r')as file:
                todos = file.readlines()

            new_todo = input("Edit your todo: ")
            todos[number] = new_todo + '\n'

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

        case "complete":
            number = int(input("What is the number of the completed todo: "))

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

            message = f"Todo {todo_to_remove} was removed from the list."
            print(message)

        case "exit":
            break
        case whatever:
            print("!!!You wrote a wrong command!!!")
print("Bye!")