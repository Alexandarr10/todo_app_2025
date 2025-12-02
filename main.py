todos = []

while True:
    user_decision = input("Type add, show, edit or exit")
    user_decision = user_decision.strip()

    match user_decision:
        case "add":
            todo = input("Enter a todo: ")
            todos.append(todo)
        case "show":
            for item in todos:
                print(item)
        case "edit":
            number = int(input("What is the number of the todo to edit: "))
            number = number - 1
            new_todo = input("Edit your todo: ")
            todos[number] = new_todo
        case "exit":
            break
        case whatever:
            print("!!!You wrote a wrong command!!!")
print("Bye!")