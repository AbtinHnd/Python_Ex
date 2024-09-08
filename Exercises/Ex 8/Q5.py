employee_data = {}

for i in range (100):
    print('Please select one of the following options:')
    print('1. Add Employee')
    print('2.Update Salary')
    print('3. Delete Employee with salary under 3000')
    print('4.Edit Employee')
    print('5.total Salary')
    print('6.Show all Employees Info')
    print('7. Exit')
    print('------------------------****-------------------------')
    chooice = input('Enter your choice: ')
    chooice = chooice.lower()
    if chooice == '1' or chooice == 'add employee':
        id = input('Give me ID for New employee:')
        id = id.lower()
        if id  == 'exit':
            break
        elif id not in employee_data.keys():
            age = int(input('give employee age: '))
            salary = int(input('give salary for employee: '))
            print('-----******------*****---------********---------------********')
            employee_data[id] = {"age": age , "salary": salary}
            print('Employee Added Successfuly')
            print(f' our employee data: {employee_data}')
            print('-----******------*****---------********---------------********')
        else:
            print('ID already exist')
            print('-----******------*****---------********---------------********')
    elif chooice == '2' or chooice == 'update salary':
        if len(employee_data) == 0:
            print('No employee data found')
            print('-----******------*****---------********---------------********')
        else:
            for id in employee_data.keys():
                if employee_data[id]['age'] > 50 :
                    employee_data[id]['salary'] = int(employee_data[id]['salary']) * 1.1
                    print('Salary Change successfuly')
                    print(f'Employees information after update: {employee_data[id]}')
                    print('-----******------*****---------********---------------********')
                else:
                    continue
    elif chooice == '3' or chooice == 'delete employee with salary under 3000':
        if len(employee_data) == 0:
            print('No employee data found')
            print('-----******------*****---------********---------------********')
        else:
            for key in list(employee_data.keys()):
                if employee_data[key]['salary'] < 3000:
                    del employee_data[key]
                    print(f'Removed Successfuly')
                    print(f' our employee data: {employee_data}')
                    print('-----******------*****---------********---------------********')
    elif chooice == '4' or chooice == 'edit employee':
        check_id = input('Enter ID to edit: ')
        if check_id in employee_data.keys():
            print('Do you want to edit what?')
            print('1. Age')
            print('2. Salary')
            print('3.Both of them')
            print('4. Exit')
            print('------------------------****-------------------------')
            edit_choice = input('Enter your choice: ')
            edit_choice = edit_choice.lower()
            if edit_choice == '1' or edit_choice == 'age':
                new_age = int(input('Give new Age:'))
                employee_data[check_id] = {"age": new_age , "salary": employee_data[id]['salary']}
                print('Age Updated Successfuly')
                print('-----******------*****---------********---------------********')
            elif edit_choice == '2' or edit_choice == 'salary':
                new_salary = int(input('Give new ssalary for Employee: '))
                employee_data[check_id] = {"age": employee_data[id]['age'] , "salary": new_salary}
                print('Salary Updated Successfuly')
                print('-----******------*****---------********---------------********')
            elif edit_choice == '3' or edit_choice == 'both of them':
                n_age = int(input('Give new Age:'))
                n_salary = int(input('Give new salary for Employee: '))
                employee_data[check_id] = {"age": n_age , "salary": n_salary}
                print('Updated Successfuly')
                print('-----******------*****---------********---------------********')
            elif edit_choice == '4' or edit_choice == 'exit':
                break
            else:
                print('Invalid Choice')
                print('-----******------*****---------********---------------********')
        else:
            print('ID not found')
            print('-----******------*****---------********---------------********')
    elif chooice == '5' or chooice == 'total salary':
        total_salary = 0
        for key in employee_data.keys():
            total_salary += employee_data[key]['salary']
        print(f'Total Salary: {total_salary}')
    elif chooice == '6' or chooice == 'show all employees info':
        print('Employee Data:')
        for key in employee_data.keys():
            print(f'our Emplpyee ID : {key}\t\t Age :{employee_data[key]["age"]}\t\t Salary: {employee_data[key]["salary"]}')
            print('-----******------*****---------********---------------********')
    elif chooice == '7' or chooice == 'exit':
        break
    else:
        print('Invalid Choice')
        print('-----******------*****---------********---------------********')

