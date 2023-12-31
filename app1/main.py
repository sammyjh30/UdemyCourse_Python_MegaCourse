# Custom functions are usually created above the main code + 2 spaces between code
def get_todos(filepath): # filepath -> parameter
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines() # var is only valid within this function. var can't be called elsewhere
    return todos_local


def write_todos(filepath, todos_arg): # Function does not need to return anything so it doesn't
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)


while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"): # Prevents issues with editing a todo with "add" in it
        todo = user_action[4:] # slicing, extracting all the characters FROM the char 4, blank after : means everything from the start point

        todos = get_todos('files/todos.txt') # 'files/todos.txt' -> argument value. could be written as (filepath='files/todos.txt')

        todos.append(todo + '\n')

        write_todos('files/todos.txt', todos)
    elif user_action.startswith("show"):         # elif Speeds up the code by reducing the number of checks -> not all checks are run after one is met
        todos = get_todos('files/todos.txt')

        # new_todos = [item.strip('\n') for item in todos]  # list comprehension

        for index, item in enumerate(todos):   # enumerate allows us to get both the index and the item
            item = item.strip('\n').title()
            row = f"{index + 1}-{item}"       # f-strings, allow more control. e.g. no spaces between chars
            print(row) # print also adds a new line

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = get_todos('files/todos.txt')

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'

            write_todos('files/todos.txt', todos)
        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos = get_todos('files/todos.txt')

            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            write_todos('files/todos.txt', todos)

            message = f"Todo {todo_to_remove} was removed from the list."
            print(message)
        except IndexError:
            print("There is no item with that number.")
            continue

    elif user_action.startswith("exit"):
        break
    else:
        print("Command is not valid.")

print("Bye!")
