todos = []

while True:
    user_action = input("Type add, show, or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'show' | 'display':            # bitwise "or"
            for item in todos:
                item = item.title()     # Can have multiple lines, must make sure indentation is consistent
                print(item)
        case 'exit':
            break
        case _:      # Doesn't need to be defined prior. Can be variable, standard practice uses _
            print("You have entered an unknown command. Please try again.")
print("Bye!")
