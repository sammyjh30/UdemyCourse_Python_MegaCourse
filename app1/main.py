
while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    #  Use if ___ in -> to allow the value to be entered with the command
    if 'add' in user_action:
        todo = user_action[4:] # slicing, extracting all the characters FROM the char 4, blank after : means everything from the start point

        with open('files/todos.txt', 'r') as file:
            todos = file.readlines()
            # Don't need to close the file using a with-context-manager

        todos.append(todo)

        with open('files/todos.txt', 'w') as file:
            file.writelines(todos)
    if 'show' in user_action:
        with open('files/todos.txt', 'r') as file:
            todos = file.readlines()

        # new_todos = [item.strip('\n') for item in todos]  # list comprehension

        for index, item in enumerate(todos):   # enumerate allows us to get both the index and the item
            item = item.strip('\n').title()
            row = f"{index + 1}-{item}"       # f-strings, allow more control. e.g. no spaces between chars
            print(row) # print also adds a new line

    if 'edit' in user_action:
        number = int(input("Number of the todo to edit: "))   # Input always outputs a string
        number = number - 1

        with open('files/todos.txt', 'r') as file:
            todos = file.readlines()

        new_todo = input("Enter new todo: ")
        todos[number] = new_todo + '\n'

        with open('files/todos.txt', 'w') as file:
            file.writelines(todos)

    if 'complete' in user_action:
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

    if 'exit' in user_action:
        break

print("Bye!")
