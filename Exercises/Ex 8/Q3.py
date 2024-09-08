student_grades = {
    'Iran': 20,
    'Houmayon': 18.5,
    'Meshkat': 15.4
}

for i in range(10):
    print(f'We have Menu of what you want to do please choose: \n')
    print('1.Add new Student')
    print('2.Delete Student with Grades below 10')
    print('3.Edit grades')
    print('4.Average Grade of all student')
    print('***         ****         ***        ****       ***')
    choose = input('which one is your choise? ')
    choose = choose.lower()

    if choose == '1' or choose == 'add new student':
        print('------------------------------------------------')
        name = input('Give me student name: ')
        if name.lower() == 'exit':
            break
        elif name in student_grades.keys():
            print(f'We want a unique name')
            continue
        else:
            grade = float(input('give student grade: '))
            if 0 < grade < 20:
                student_grades[name] = grade
                print(f'{student_grades}')
                print('------------------------------------------------')
            else:
                 print(f'Give a Valid Grade')
                 continue

    elif choose == '2' or choose == 'delete student with grades below 10':
        to_delete = [name for name, grade in student_grades.items() if grade < 10]
        for name in to_delete:
            del student_grades[name]

        print(f'{student_grades}')
        print('------------------------------------------------')
    elif choose == '3' or choose == 'edit grades':
        print('------------------------------------------------')
        name = input('Give me student name: ')
        if name.lower() == 'exit':
            break
        else:
            if name in student_grades.keys():
                if 0 < grade < 20:
                    grade = float(input('give new grade: '))
                    student_grades[name] = grade
                    print(f'Grade successfully Changed!!')
                else:
                    print(f'It is out of bound!!')
                    continue
    elif choose == '4' or choose == 'average grade of all student':
        if student_grades:
            avg = sum(student_grades.values()) / len(student_grades)
            print(f'Our grades Avarage is {avg}')
            print(student_grades)
        else:
            print(f'No Student in list!!')

    elif choose =='exit':
        break

    else:
        print('Invalid choice. Please select a Correct choice')









