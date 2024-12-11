import mysql.connector
from mysql.connector import errorcode

# Establish database connection
mydb = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="Abtin.abtin1",
    database="meaw",
    auth_plugin="mysql_native_password"
)
mycursor = mydb.cursor()

# Table creation statements
user = """
    create table if not exists user(
        user_id int not null auto_increment,
        username varchar(255) not null,
        password varchar(255) not null,
        primary key(user_id)
    );"""

employee = """
    create table if not exists employee(
        emp_id int not null auto_increment,
        first_name varchar(255) not null,
        last_name varchar(255) not null,
        email varchar(255) not null,
        primary key(emp_id)
    );"""

book = """
    create table if not exists book(
        book_id int not null auto_increment,
        book_name varchar(255) not null,
        author varchar(255) not null,
        publication_date varchar(255) not null,
        genre varchar(255) not null,
        primary key(book_id)
    );"""

# Execute table creation
def create_table(query):
    try:
        mycursor.execute(query)
        print("Table created successfully (if not already existing).")
    except mysql.connector.Error as err:
        print(f"Error: {err}")

# Create the tables if they don't exist
create_table(user)
create_table(employee)
create_table(book)

class UserManagement:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def register(self):
        command = """
            insert into user(username, password)
            values(%s, %s)
        """
        value = (self.username, self.password)
        mycursor.execute(command, value)
        mydb.commit()

    def login(self):
        command = """
            select * from user
            where username = %s and password = %s
        """
        value = (self.username, self.password)
        mycursor.execute(command, value)
        result = mycursor.fetchall()
        if len(result) == 0:
            print("Invalid username or password")
        else:
            print("Login successful")

    def remove(self):
        command = """
            delete from user
            where username = %s
        """
        value = (self.username,)
        mycursor.execute(command, value)
        mydb.commit()

    def show_profile(self):
        command = """
            select * from user
            where username = %s
        """
        value = (self.username,)
        mycursor.execute(command, value)
        result = mycursor.fetchall()
        for user_id, username, password in result:
            print(f"User ID: {user_id}\nUsername: {username}\nPassword: {password}")

class EmployeeManagement:
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def add_employee(self):
        command = """
            insert into employee(first_name, last_name, email)
            values(%s, %s, %s)
        """
        value = (self.first_name, self.last_name, self.email)
        mycursor.execute(command, value)
        mydb.commit()

    def show_profile(self):
        command = """
            select * from employee
            where email = %s
        """
        value = (self.email,)
        mycursor.execute(command, value)
        result = mycursor.fetchall()
        for emp_id, first_name, last_name, email in result:
            print(f"Employee ID: {emp_id}\nFirst Name: {first_name}\nLast Name: {last_name}\nEmail: {email}")

class BookManagement:
    def __init__(self, book_name, author, publication_date, genre):
        self.book_name = book_name
        self.author = author
        self.publication_date = publication_date
        self.genre = genre

    def add_book(self):
        command = """
            insert into book(book_name, author, publication_date, genre)
            values(%s,%s,%s,%s)
        """
        value = (self.book_name, self.author, self.publication_date, self.genre)
        mycursor.execute(command, value)
        mydb.commit()

    def update_book(self):
        command = """
        update book
            set book_name = %s, 
                publication_date = %s,
                genre = %s
            where author = %s   
        """
        value = (self.book_name, self.publication_date, self.genre, self.author)
        mycursor.execute(command, value)
        mydb.commit()

    def search(self):
        command = """
            select * from book
            where book_name = %s
        """
        value = (self.book_name,)
        mycursor.execute(command, value)
        result = mycursor.fetchall()
        for book_id, book_name, author, publication_date, genre in result:
            print(f"Book ID: {book_id}\nBook Name: {book_name}\nAuthor: {author}\nPublication Date: {publication_date}\nGenre: {genre}")


def main():
    user1 = UserManagement("abtin", "password123")
    user1.register()
    user1.login()
    user1.show_profile()
    user1.remove()

    employee1 = EmployeeManagement("John", "Doe", "john.doe@example.com")
    employee1.add_employee()
    employee1.show_profile()

    book1 = BookManagement("The Great Gatsby", "F. Scott Fitzgerald", "1925", "Fiction")
    book1.add_book()
    book1.search()
    book1.update_book()


if __name__ == "__main__":
    main()
