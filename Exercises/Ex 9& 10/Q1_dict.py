from datetime import datetime

to_do = {}


def add_task():
    print(f'- - - - - - -- -- -  -  --  - -- - - -  - - - - - - - - - - - - -- - - - -')
    x = input('Enter Task Name: ')
    if x == 'exit':
        return
    elif x not in to_do:
        to_do[x] = {"date": None , "status": False}
        print(f'Task Added \n')
        print(f' - - - - - - -- -- -  -  --  - -- - - -  - - - - - - - - - - - - -- - - - -')

    else:
        print(f'Task Already Exists')
def display_prod():
    if not to_do:
        print('No tasks found.')

    for idx,(x,details) in enumerate(to_do.items()):
        print(f' - - - - - - -- -- -  -  --  - -- - - -  - - - - - - - - - - - - -- - - - -')
        print(f"{idx + 1}.Task ==> {x} ,  status ==> {to_do[x]['status']} , duration ==> {to_do[x]['date']}")
        print(f' - - - - - - -- -- -  -  --  - -- - - -  - - - - - - - - - - - - -- - - - -')
def remove_task():
    print(f'- - - - - - -- -- -  -  --  - -- - - -  - - - - - - - - - - - - -- - - - -')
    x = input('Enter Task Name: ')
    if x == 'exit':
        return
    elif x in to_do:
        del to_do[x]
        print(f'Task Removed')
        print(f' - - - - - - -- -- -  -  --  - -- - - -  - - - - - - - - - - - - -- - - - -')
    else:
        print(f'Task Not Found')
def edit_task():
    print(f'- - - - - - -- -- -  -  --  - -- - - -  - - - - - - - - - - - - -- - - - -')
    x = input('Enter Task Name: ')
    if x == 'exit':
        return
    elif x in to_do:
        v = input('Enter New Task Name: ')
        to_do[v] =to_do.pop(x)
        print(f'Task Edited')
        print(f' - - - - - - -- -- -  -  --  - -- - - -  - - - - - - - - - - - - -- - - - -')
    else:
        print(f'Task Not Found!')
def search_task():
    print(f'- - - - - - -- -- -  -  --  - -- - - -  - - - - - - - - - - - - -- - - - -')
    x = input('Enter Task Name: ')
    if x == 'exit':
        return
    elif x in to_do:
        det = to_do[x]
        print(f"Task:{x}, Status {det['status']},date{det['date']}")
        print(f'- - - - - - -- -- -  -  --  - -- - - -  - - - - - - - - - - - - -- - - - -')
    else:
        print(f'Task Not Found!')
def mark_done():
    print(f'- - - - - - -- -- -  -  --  - -- - - -  - - - - - - - - - - - - -- - - - -')
    x = input('Enter Task Name: ')
    if x == 'exit':
        return
    elif x in to_do:
        start = input('Enter Start Time(in 24 Hour) : ')
        end = input('Enter End Time (in 24 Hour Format): ')
        if end > start:
            start_time = datetime.strptime(start, '%H:%M')
            end_time = datetime.strptime(end, '%H:%M')
            diffr = end_time - start_time
            diffr_in_minutes = diffr.total_seconds() // 60
            to_do[x]['date'] = diffr_in_minutes
            to_do[x]['status'] = True
            print(f'Task Done in {diffr_in_minutes} minute')
            print(f'- - - - - - -- -- -  -  --  - -- - - -  - - - - - - - - - - - - -- - - - -')
        else:
            print(f"End Time Can't be lower that Start")

    else:
        print(f'Task Not Found!')

def details():
    num_task = len(to_do)
    total_minutes = sum(details['date'] for details in to_do.values() if details['date'] is not None)
    hours = int(total_minutes // 60)
    minutes = int(total_minutes % 60)
    complate_task = sum(1 for details in to_do.values() if details['status'])
    uncomplate_task = num_task - complate_task

    print(f'- - - - - - -- -- -  -  --  - -- - - -  - - - - - - - - - - - - -- - - - -')
    print(f'Number of all tasked you Register: {num_task}')
    print(f'Total Hours you spend for do Tasks: {hours} Hour and {minutes} minute')
    print(f'Number of Complated Tasks: {complate_task}')
    print(f'Number of Uncomplated Tasks: {uncomplate_task}')
    print(f'- - - - - - -- -- -  -  --  - -- - - -  - - - - - - - - - - - - -- - - - -')

def help_():
    print(f'- - - - - - -- -- -  -  --  - -- - - -  - - - - - - - - - - - - -- - - - -')
    print(f' in "Add Task" you should give task in input ')
    print(f'in "Display all products" we Display all date with their details (task,Status,date)')
    print(f' in "Remove Task" you should give task name and then task will remove from data ')
    print(f' in "Edit Task" you should give name that you want to edit and'
          f' then if exist you can give new name that you want to be ')
    print(f' in "search Task" you should give task name and we display the details of Task')
    print(f' in "Mark as Done" when you Finish your task you choose this part and set start and end time ')
    print(f' in "Display Details" we will show you all details you need to know about Tasks you register')
    print(f' when you write "exit" in code we will interpert code')
    print(f'- - - - - - -- -- -  -  --  - -- - - -  - - - - - - - - - - - - -- - - - -')





for i in range(201):
    print(f'- - - - - - -- -- -  -  --  - -- - - -  - - - - - - - - - - - - -- - - - -')
    print(f'1. Add Task')
    print(f'2.Display All Products')
    print(f'3.Remove Task')
    print(f'4.Edit Task')
    print(f'5.Search Task')
    print(f'6.Mark Task as Done')
    print(f'7.Display Details')
    print(f'8.Help')
    print(f'9.Exit')
    print(f' - - - - - - -- -- -  -  --  - -- - - -  - - - - - - - - - - - - -- - - - -')
    choice = input('Enter your choice(number or name): ')
    choice = choice.lower()
    if choice == '1' or choice == 'add task':
        add_task()
    elif choice == '2' or choice == 'display all tasks':
        display_prod()
    elif choice == '3' or choice == 'remove task':
        remove_task()
    elif choice == '4' or choice == 'edit task':
        edit_task()
    elif choice == '5' or choice == 'search task':
        search_task()
    elif choice == '6' or choice == 'mark task as done':
        mark_done()
    elif choice == '7' or choice == 'Display Details':
        details()
    elif choice == '8' or choice == 'help':
        help_()
    elif choice == '9' or choice == 'exit':
        break




