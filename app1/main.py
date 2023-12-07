
while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ") + "\n"  # to add new lines in txt file

            with open('files/todos.txt', 'r') as file:
                todos = file.readlines()
                # Don't need to close the file using a with-context-manager

            todos.append(todo)

            with open('files/todos.txt', 'w') as file:
                file.writelines(todos)
        case 'show':
            with open('files/todos.txt', 'r') as file:
                todos = file.readlines()

            # new_todos = [item.strip('\n') for item in todos]  # list comprehension

            for index, item in enumerate(todos):   # enumerate allows us to get both the index and the item
                item = item.strip('\n').title()
                row = f"{index + 1}-{item}"       # f-strings, allow more control. e.g. no spaces between chars
                print(row) # print also adds a new line
        case 'edit':
            number = int(input("Number of the todo to edit: "))   # Input always outputs a string
            number = number - 1

            with open('files/todos.txt', 'r') as file:
                todos = file.readlines()

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'

            with open('files/todos.txt', 'w') as file:
                file.writelines(todos)

        case 'complete':
            number = int(input("Number of the todo to complete: "))

            with open('files/todos.txt', 'r') as file:
                todos = file.readlines()

            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            with open('files/todos.txt', 'w') as file:
                file.writelines(todos)

            message = f"Todo {todo_to_remove} was removed from the list."
            print(message)
        case 'exit':
            break
        case _:      # Doesn't need to be defined prior. Can be variable, standard practice uses _
            print("You have entered an unknown command. Please try again.")
print("Bye!")
