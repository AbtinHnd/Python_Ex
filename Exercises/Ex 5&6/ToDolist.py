from datetime import datetime


name = []
date = []
status = []
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
        print(f'- - - - - - -- -- -  -  --  - -- - - -  - - - - - - - - - - - - -- - - - -')
        x = (input('Enter Task Name: '))
        if x not in name:
            name.append(x)
            date.append(None)
            status.append(False)
            print(f'Task Added \n')
            print(f' - - - - - - -- -- -  -  --  - -- - - -  - - - - - - - - - - - - -- - - - -')
        elif x == 'exit':
            break
        else:
            print(f'Task Already Exists')
    elif choice == '2' or choice == 'display all tasks':
            for i in range(len(name)):
                print(f' - - - - - - -- -- -  -  --  - -- - - -  - - - - - - - - - - - - -- - - - -')
                print(f'{i+1}.Task ==> {name[i]} ,  status ==> {status[i]} , duration ==> {date[i]}')
                print(f' - - - - - - -- -- -  -  --  - -- - - -  - - - - - - - - - - - - -- - - - -')
    elif choice == '3' or choice == 'remove task':
        print(f'- - - - - - -- -- -  -  --  - -- - - -  - - - - - - - - - - - - -- - - - -')
        x = input('Enter Task Name: ')
        if x in name:
            i = name.index(x)
            name.pop(i)
            date.pop(i)
            status.pop(i)

            print(f'Task Removed')
            print(f' - - - - - - -- -- -  -  --  - -- - - -  - - - - - - - - - - - - -- - - - -')
        elif x == 'exit':
            break
        else:
            print(f'Task Not Found')
    elif choice == '4' or choice == 'edit task':
        print(f'- - - - - - -- -- -  -  --  - -- - - -  - - - - - - - - - - - - -- - - - -')
        x = input('Enter Task Name: ')
        if x in name:
            i = name.index(x)
            name[i] = input('Enter New Task Name: ')
            print(f'Task Edited')
            print(f' - - - - - - -- -- -  -  --  - -- - - -  - - - - - - - - - - - - -- - - - -')
        elif x == 'exit':
            break
        else:
            print(f'Task Not Found!')
    elif choice == '5' or choice == 'search task':
        print(f'- - - - - - -- -- -  -  --  - -- - - -  - - - - - - - - - - - - -- - - - -')
        x = input('Enter Task Name: ')
        if x in name:
            i = name.index(x)
            print(f'{name[i]} {status[i]} {date[i]}')
            print(f'- - - - - - -- -- -  -  --  - -- - - -  - - - - - - - - - - - - -- - - - -')
        elif x == 'exit':
            break
        else:
            print(f'Task Not Found!')
    elif choice == '6' or choice == 'mark task as done':
        print(f'- - - - - - -- -- -  -  --  - -- - - -  - - - - - - - - - - - - -- - - - -')
        x = input('Enter Task Name: ')
        if x in name:
            i = name.index(x)
            start = input('Enter Start Time(in 24 Hour) : ')
            end = input('Enter End Time (in 24 Hour Format): ')
            if end> start:
                    start_time = datetime.strptime(start, '%H:%M')
                    end_time = datetime.strptime(end, '%H:%M')
                    diffr = end_time - start_time
                    diffr_in_minutes = diffr.total_seconds() // 60
                    date[i] = diffr_in_minutes
                    status[i] = True
                    print(f'Task Done in {diffr_in_minutes} minute')
                    print(f'- - - - - - -- -- -  -  --  - -- - - -  - - - - - - - - - - - - -- - - - -')
            else:
                print(f"End Time Can't be lower that Start")

        elif x == 'exit':
            break
        else:
            print(f'Task Not Found!')
    elif choice == '7' or choice == 'Display Details':
        num_task = len(name)
        list1 = list(filter(lambda h: h is not None, date))
        total_minutes = sum(list1)
        hours = int(total_minutes // 60)
        minutes = int(total_minutes % 60)
        complate_task = status.count(True)
        uncomplate_task = status.count(False)

        print(f'- - - - - - -- -- -  -  --  - -- - - -  - - - - - - - - - - - - -- - - - -')
        print(f'Number of all tasked you Register: {num_task}')
        print(f'Total Hours you spend for do Tasks: {hours} Hour and {minutes} minute')
        print(f'Number of Complated Tasks: {complate_task}')
        print(f'Number of Uncomplated Tasks: {uncomplate_task}')
        print(f'- - - - - - -- -- -  -  --  - -- - - -  - - - - - - - - - - - - -- - - - -')

    elif choice == '8' or choice == 'help':
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
    elif choice == '9' or choice == 'exit':
        break





