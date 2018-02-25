
todo_list = []
print("What are we working on today?")
print("enter 'DONE' to stop adding items.")


def print_list():
    print("Here is your list: ")
    for item in todo_list:
        print(item)


while True:
    new_item = input("> ")
if new_item == 'DONE':
    break
elif new_item == 'HELP':
    print("enter 'DONE' to exit program \n ")
    print("enter 'SHOW' to see the items currently on your shopping list\n")
    print("enter 'HELP' to see what special commands are available\n")
elif new_item == 'SHOW':
    print_list()
elif new_item != 'DONE':
    todo_list.append(new_item)

print_list()
