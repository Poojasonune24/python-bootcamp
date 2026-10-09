User_List = []


def Create_to_do_list():
 
    user_input = int(input("(1) to add an item\n(2) to delete an item at index \n(3) to remove the last item \n(4) to sort the list \n(5) To print the list \n(6) Exit the app:  "))

    if user_input == 1:
        add_items()
    elif user_input == 2:
        Delete_entry()
    elif user_input == 3:
        Remove_last_element()
    elif user_input == 4:
        Sort_list()
    elif user_input == 5:
        Print_list()
    elif user_input == 6:
        Exit_app()
    else:
        Create_to_do_list()

def add_items():  
    user_list_item = input("Enter your todo list task/Enter -1 for go to prev menu: ")

    while user_list_item != "-1":
        User_List.append(user_list_item)
        user_list_item = input("Enter your todo list task/Enter -1 for go to prev menu: ")


    if user_list_item == "-1":
        Create_to_do_list()

def Delete_entry():
    index = int(input("Enter the index for deleting the entry: "))
    User_List.pop(index)
    print(User_List)

def Sort_list():
    User_List.sort()
    print(User_List)

def Remove_last_element():
    User_List.pop()
    print(User_List)

def Print_list():
    print(User_List)

def Exit_app():
    print("App is Closed now")

Create_to_do_list()





