import mysql.connector

mydb = mysql.connector.connect(

)

mycursor = mydb.cursor()

student = """
    CREATE TABLE IF NOT EXISTS student (
        student_id INT NOT NULL AUTO_INCREMENT,
        first_name VARCHAR(255),
        last_name VARCHAR(255) NOT NULL,
        DAtaOfBirth VARCHAR(255),
        Email VARCHAR(255),
        PRIMARY KEY (student_id)
    );
"""
mycursor.execute(student)

coursesField = """
    CREATE TABLE IF NOT EXISTS CoursesField (
        course_id INT NOT NULL AUTO_INCREMENT,
        Course_name VARCHAR(255),
        Instructor VARCHAR(255),
        PRIMARY KEY (course_id)
    );
"""
mycursor.execute(coursesField)

enrollment = """
    CREATE TABLE IF NOT EXISTS enrollment (
        enrollment_id INT NOT NULL AUTO_INCREMENT,
        enrollmentDate VARCHAR(255),
        student_id INT NOT NULL,
        course_id INT NOT NULL,
        PRIMARY KEY (enrollment_id),
        FOREIGN KEY (student_id) REFERENCES student(student_id),
        FOREIGN KEY (course_id) REFERENCES CoursesField(course_id)
    );
"""
mycursor.execute(enrollment)

command1 = """
    INSERT INTO student (first_name, last_name, DAtaOfBirth, Email)
    VALUES (%s, %s, %s, %s)
"""
students = [
    ("abtin", "Hosseinnezhad", "2003-04-10", "Iran.Iran@gmail.com"),
    ("Ali", "Reza", "2002-03-15", "ali.reza@gmail.com"),
    ("Sara", "Zamani", "2001-06-20", "sara.zamani@gmail.com"),
]

for student_data in students:
    try:
        mycursor.execute(command1, student_data)
    except mysql.connector.Error as err:
        print(f"Error inserting into Student table: {err}")

command2 = """
INSERT INTO CoursesField (Course_name, Instructor)
VALUES (%s, %s)
"""
courses = [
    ("python", "MS.Bakhshande"),
    ("java", "Dr.Smith"),
    ("web development", "Dr.Johnson"),
]

for course_data in courses:
    try:
        mycursor.execute(command2, course_data)
    except mysql.connector.Error as err:
        print(f"Error inserting into CoursesField table: {err}")

command3 = """
    INSERT INTO enrollment (enrollmentDate, student_id, course_id)
    VALUES (%s, %s, %s)
"""
enrollments = [
    ("2024-05-12", 1, 1),
    ("2024-05-13", 2, 2),
    ("2024-05-15", 3, 3),
]

for enrollment_data in enrollments:
    try:
        mycursor.execute(command3, enrollment_data)
    except mysql.connector.Error as err:
        print(f"Error inserting into Enrollment table: {err}")

mydb.commit()


find_student = """
    SELECT student.first_name, student.last_name, COUNT(enrollment.course_id) AS course_count 
    FROM student
    LEFT JOIN enrollment ON student.student_id = enrollment.student_id 
    GROUP BY student.student_id
    ORDER BY student.first_name;
"""
mycursor.execute(find_student)


student_data = mycursor.fetchall()
for first_name, last_name, course_count in student_data:
    print(f"{first_name} {last_name}: {course_count} courses")


query = """
DELETE FROM enrollment
WHERE student_id IN (
    SELECT student_id
    FROM (
        SELECT student_id
        FROM enrollment
        GROUP BY student_id
        HAVING COUNT(course_id) < 2
    ) AS subquery
);
"""
mycursor.execute(query)
mydb.commit()

final_query = """DELETE FROM student
WHERE student_id IN (
    SELECT student_id
    FROM (
        SELECT student_id
        FROM enrollment
        GROUP BY student_id
        HAVING COUNT(course_id) < 2
    ) AS subquery
);
"""
mycursor.execute(final_query)
mydb.commit()


#Update
update_query = """
    UPDATE CoursesField
    SET Course_name = 'Python'
    WHERE Course_name LIKE '%Java%';
"""
mycursor.execute(update_query)
mydb.commit()

select_query = """
    SELECT course_id, Course_name
    FROM CoursesField
    WHERE Course_name LIKE '%Python%';
"""
mycursor.execute(select_query)


for course_id, course_name in mycursor.fetchall():
    print(f"Course ID: {course_id}, Course Name: {course_name}")

mycursor.close()
