
while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"): # Prevents issues with editing a todo with "add" in it
        todo = user_action[4:] # slicing, extracting all the characters FROM the char 4, blank after : means everything from the start point

        with open('files/todos.txt', 'r') as file:
            todos = file.readlines()
            # Don't need to close the file using a with-context-manager

        todos.append(todo + '\n')

        with open('files/todos.txt', 'w') as file:
            file.writelines(todos)
    elif user_action.startswith("show"):         # elif Speeds up the code by reducing the number of checks -> not all checks are run after one is met
        with open('files/todos.txt', 'r') as file:
            todos = file.readlines()

        # new_todos = [item.strip('\n') for item in todos]  # list comprehension

        for index, item in enumerate(todos):   # enumerate allows us to get both the index and the item
            item = item.strip('\n').title()
            row = f"{index + 1}-{item}"       # f-strings, allow more control. e.g. no spaces between chars
            print(row) # print also adds a new line

    elif user_action.startswith("edit"):
        number = int(user_action[5:])
        number = number - 1

        with open('files/todos.txt', 'r') as file:
            todos = file.readlines()

        new_todo = input("Enter new todo: ")
        todos[number] = new_todo + '\n'

        with open('files/todos.txt', 'w') as file:
            file.writelines(todos)

    elif user_action.startswith("complete"):
        number = int(user_action[9:])

        with open('files/todos.txt', 'r') as file:
            todos = file.readlines()

        index = number - 1
        todo_to_remove = todos[index].strip('\n')
        todos.pop(index)

        with open('files/todos.txt', 'w') as file:
            file.writelines(todos)

        message = f"Todo {todo_to_remove} was removed from the list."
        print(message)

    elif user_action.startswith("exit"):
        break
    else:
        print("Command is not valid.")

print("Bye!")
