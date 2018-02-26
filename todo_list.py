
todo_list = []
print("What are we working on today?")
print("enter 'DONE' to stop adding items.")


def print_help():
    print("enter 'DONE' to exit program \
    enter 'SHOW' to see the items currently on your shopping list\
    enter 'HELP' to see what special commands are available")


def print_list():
    print("Here is your list: ")
    for item in todo_list:
        print(item)


print_help()

while True:
    new_item = input("> ")
    if new_item == 'HELP':
        print_help()
    elif new_item == 'DONE':
        break
    elif new_item == 'SHOW':
        print_list()
    todo_list.append(new_item)

print_list()
