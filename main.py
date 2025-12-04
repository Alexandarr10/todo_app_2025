todos = []

while True:
    user_decision = input("Type add, show, edit, exit or complete")
    user_decision = user_decision.strip()

    match user_decision:
        case "add":
            todo = input("Enter a todo: ")
            todos.append(todo)
        case "show":
            for index, item in enumerate(todos):
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