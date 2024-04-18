#Write a python program to add, delete, update employees into sql table
import mysql.connector

# Connect to the database
connection = mysql.connector.connect(
    
    host="localhost",
    port=3306, 
    user="superuser",
    password="9130694991",
    database="iotdb"

)
def show():
    query = "select * from employees;"
    cursor = connection.cursor()
    cursor.execute(query)
    for row in cursor:
        print(row)
    cursor.close()

def exec(query):

    cursor = connection.cursor()
    cursor.execute(query)
   
    connection.commit()
    cursor.close()

def add():
    empid = input("Enter empid : ")
    name = input("Enter name : ")
    department= input("Enter department : ")
    email= input("Enter email :")
    salary = int(input("Enter salary : "))
    dateofjoining = input("Enter date of joining : ")

    query = f"insert into employees values( '{empid}','{name}', '{department}', '{email}', {salary}, '{dateofjoining}');"
    exec(query)

def delete():
    empid = input("Enter empid : ")
    query = f"delete from employees where empid = '{empid}';"
    exec(query)

def update():
    empid = input("Enter empid to be updated: ")
    department= input("Enter department : ")
    email= input("Enter email :")
    salary = int(input("Enter salary : "))

    query = f"update employees set department = %s , email = %s, salary = %s where empid = %s ;"
    val = (department,email,salary,empid)
    
    cursor = connection.cursor()
    cursor.execute(query,val)
    connection.commit()
    cursor.close()

  

 

while True:
    print("Employees table ")
    show()
    print("1. Add employee")
    print("2. Delete employee")
    print("3. Update employee")
    print("4. Exit")
    choice = int(input("Enter your choice : "))
    if choice == 1:
        add()
        show()

    elif choice == 2:
        delete()
        show()

    elif choice == 3:
        update()
        show()

    elif choice == 4:
        break

    else:
        print("Invalid choice")


#close the connection with mysql server 
connection.close()
