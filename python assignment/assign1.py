import csv
import mysql.connector
from mysql.connector import errorcode

class Employee:
    def __init__(self, employee_id, email, name, phone, pf_id, date_of_joining, date_of_birth, department):
        self.employee_id = employee_id
        self.email = email
        self.name = name
        self.phone = phone
        self.pf_id = pf_id
        self.date_of_joining = date_of_joining
        self.date_of_birth = date_of_birth
        self.department = department

    @staticmethod
    def is_email_valid(email):
        import re
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return re.match(pattern, email) is not None

    @staticmethod
    def is_phone_number_valid(phone):
        return phone.isdigit() and len(phone) >= 10

def create_employee_table(cursor):
    try:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Employees (
                EmployeeId INT AUTO_INCREMENT,
                Email VARCHAR(255) UNIQUE,
                Name VARCHAR(255),
                Phone VARCHAR(15),
                PfId VARCHAR(255) UNIQUE,
                DateOfJoining DATE,
                DateOfBirth DATE,
                Department VARCHAR(255),
                PRIMARY KEY (EmployeeId)
            )
        """)
        print("Employee table created successfully.")
    except mysql.connector.Error as err:
        print(f"Error creating employee table: {err}")

def add_employee(cursor):
    print("Enter employee details:")
    employee_id = input("Employee Id: ")
    email = input("Email: ")
    name = input("Name: ")
    phone = input("Phone: ")
    pf_id = input("Pf Id: ")
    date_of_joining = input("Date of Joining (YYYY-MM-DD): ")
    date_of_birth = input("Date of Birth (YYYY-MM-DD): ")
    department = input("Department: ")

    while not Employee.is_email_valid(email):
        print("Invalid email address. Please enter a valid email.")
        email = input("Email: ")

    while not Employee.is_phone_number_valid(phone):
        print("Invalid phone number. Please enter a valid phone number (at least 10 digits).")
        phone = input("Phone: ")

    try:
        cursor.execute("""
            INSERT INTO Employees (EmployeeId, Email, Name, Phone, PfId, DateOfJoining, DateOfBirth, Department)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """, (employee_id, email, name, phone, pf_id, date_of_joining, date_of_birth, department))
        print("Employee added successfully.")
    except mysql.connector.Error as err:
        print(f"Error adding employee: {err}")

def read_employees(cursor):
    try:
        cursor.execute("SELECT * FROM Employees")
        employees = cursor.fetchall()

        if employees:
            print("Employee Id\tEmail\t\t\tName\t\tPhone\t\tPf Id\tDate of Joining\tDate of Birth\tDepartment")
            print("-------------------------------------------------------------------------------------------------------------------")
            for employee in employees:
                print("\t".join(str(field) for field in employee))
        else:
            print("No employees found.")
    except mysql.connector.Error as err:
        print(f"Error reading employees: {err}")


def update_employee_phone_numbers(cursor):
    try:
        cursor.execute("SELECT EmployeeId, Phone FROM Employees")
        employees = cursor.fetchall()

        for employee in employees:
            employee_id, current_phone = employee
            new_phone = input(f"Enter new phone number for employee {employee_id}: ")

            while not Employee.is_phone_number_valid(new_phone):
                print("Invalid phone number. Please enter a valid phone number (at least 10 digits).")
                new_phone = input(f"Enter new phone number for employee {employee_id}: ")

            try:
                cursor.execute("UPDATE Employees SET Phone = %s WHERE EmployeeId = %s", (new_phone, employee_id))
            except mysql.connector.Error as err:
                print(f"Error updating phone number for employee {employee_id}: {err}")

        print("Employee phone numbers updated successfully.")
    except mysql.connector.Error as err:
        print(f"Error retrieving employees: {err}")


def get_employees_with_joining_year(cursor, year):
    try:
        cursor.execute("SELECT * FROM Employees WHERE YEAR(DateOfJoining) = %s", (year,))
        return cursor.fetchall()
    except mysql.connector.Error as err:
        print(f"Error retrieving employees with joining year {year}: {err}")
        return []


def write_employees_to_csv(employees):
    if employees:
        file_path = "employees.csv"
        with open(file_path, "w", newline="") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow([
                "Employee Id", "Email", "Name", "Phone", "Pf Id", "Date of Joining",
                "Date of Birth", "Department"
            ])
            writer.writerows(employees)
        print("Employees written to CSV file successfully.")
    else:
        print("No employees found to write to CSV.")


def main():
    try:
        connection = mysql.connector.connect(
            host="SHTLP0145",
            user="root",
            password="Chetna@1997",
            database="py_database"
        )

        cursor = connection.cursor()
        create_employee_table(cursor)

        while True:
            print("\n1. Add Employee")
            print("2. Read Employees")
            print("3. Update Employee Phone Numbers")
            print("4. Get Employees with Joining Year 2021 and Write to CSV")
            print("5. Exit")

            option = input("Select an option: ")

            if option == "1":
                add_employee(cursor)
            elif option == "2":
                read_employees(cursor)
            elif option == "3":
                update_employee_phone_numbers(cursor)
            elif option == "4":
                employees = get_employees_with_joining_year(cursor, 2021)
                write_employees_to_csv(employees)
            elif option == "5":
                break
            else:
                print("Invalid option. Please try again.")

        cursor.close()
        connection.close()
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Error: Invalid credentials. Please check your MySQL username and password.")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Error: The specified database does not exist.")
        else:
            print(f"MySQL Error: {err}")


if __name__ == "__main__":
    main()