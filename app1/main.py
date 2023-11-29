
while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ") + "\n"  # to add new lines in txt file

            file = open('todos.txt', 'r')   # r = read -> remember the cursor moves to the end of the file
            todos = file.readlines()
            file.close()

            todos.append(todo)

            file = open('todos.txt', 'w') # w = write overwrites contents
            file.writelines(todos)
            file.close()
        case 'show':
            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()

            for index, item in enumerate(todos):   # enumerate allows us to get both the index and the item
                item = item.title()
                row = f"{index + 1}-{item}"       # f-strings, allow more control. e.g. no spaces between chars
                print(row) # print also adds a new line
        case 'edit':
            number = int(input("Number of the todo to edit: "))   # Input always outputs a string
            number = number - 1
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo
        case 'complete':
            number = int(input("Number of the todo to complete: "))
            todos.pop(number - 1)                # with pop(), default index is -1 = the last item on the list
        case 'exit':
            break
        case _:      # Doesn't need to be defined prior. Can be variable, standard practice uses _
            print("You have entered an unknown command. Please try again.")
print("Bye!")
