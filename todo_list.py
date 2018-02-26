
todo_list = []
print("What are we working on today?")


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
#    try:    THIS IS NOT WORKING, I'm back to the same problem as with the original break. It can't seem to access the new_item creation
#        new_item = input("> ")
#    except NameError:
#        print("Not the right format")
    if new_item == 'HELP':
        print_help()
    elif new_item == 'DONE':
        break
    elif new_item == 'SHOW':
        print_list()
    elif new_item != 'SHOW''HELP''DONE':
        todo_list.append(new_item)

print_list()
