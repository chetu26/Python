
import csv
import mysql.connector

class Employee:  
    #creating constructor for connection with mysql
    def __init__(self):

        self.connection= mysql.connector.connect(
        host="localhost",
        user="root",
        password="Chetna@1997",
        database="ORG"
        )
        self.cursor= self.connection.cursor()

     #taking values from user   

    def setter(self,employee_id,email,name,phone,pf_id,DOJ,DOB,department):
        self.employee_id = employee_id
        self.email = email
        self.is_email_valid()
        self.name = name
        self.phone = phone
        self.is_phone_number_valid()
        self.phone = phone
        self.pf_id = pf_id
        self.DOJ = DOJ
        self.DOB = DOB
        self.department = department

        #validation for email

    def is_email_valid(self):
        import re
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if not( re.match(pattern, self.email) ):
         while not( re.match(pattern, self.email) ):
            self.email=input("Enter valid email ")

     #validation for phone number       

    def is_phone_number_valid(self):

     if not( self.phone.isdigit() and len(self.phone) >= 10):
         while not(self.phone.isdigit() and len(self.phone) >= 10):
             self.phone=input("Enter valid phone ")

   #creating table 
    def create_employee_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Employees (
                EmployeeId INT AUTO_INCREMENT,
                Email VARCHAR(25) UNIQUE,
                Name VARCHAR(25),
                Phone VARCHAR(35),
                PfID int,
                DOJ DATE,
                DOB DATE,
                Department VARCHAR(255),
                PRIMARY KEY (EmployeeId)
            )
        """)
        print("Table created")

       #adding employee data into mysql database 

    def add(self):
      
       self.cursor.execute("""
            INSERT INTO Employees (EmployeeId, Email, Name, Phone, PfId, DOJ, DOB, Department)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """, (self.employee_id, self.email, self.name, self.phone, self.pf_id, self.DOJ, self.DOB, self.department))
       
       self.connection.commit()
       print("Employee added successfully.")
   
    #reading database on console
    def read(self):
        self.cursor.execute("SELECT * FROM Employees")
        employees = self.cursor.fetchall()

        if employees:
            temp=["EmployeeId Email  Name  Phone  Pf ID date of Joining  Date of Birth  Department"]
            print(temp)
            for employee in employees:
                row=[x for x in employee ]
                print(row,'\n')
        else:
            print("No employees found.")


    #updating phone number using employee id
    def update(self):
       
       
       eid=int(input("Enter employee id "))
       self.cursor.execute("SELECT EmployeeID FROM Employees ")
       tuple= self.cursor.fetchall()
       temp=list()
       for x in range(len(tuple)):
           temp.append(tuple[x][0])

       if eid in temp:
        self.phone = input("Enter new phone number for employee: ")
        self.is_phone_number_valid()     
        self.cursor.execute("UPDATE Employees SET Phone = %s WHERE EmployeeId = %s", (self.phone, eid))
        self.connection.commit()      
       else:
           print("Invalid Employee ID")

    def get_employees(self):
        self.cursor.execute("SELECT * FROM Employees WHERE YEAR(DOJ) = %s", (2021,))
        self.employees= self.cursor.fetchall()

    def write_employees_to_csv(self):
     if self.employees:
        file_path = "employees.csv"
        with open(file_path, "w", newline="") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow([
                "Employee Id", "Email", "Name", "Phone", "Pf Id", "Date of Joining",
                "Date of Birth", "Department"
            ])
            writer.writerows(self.employees)
        print("Employees written to CSV file successfully.")
     else:
        print("No employees found to write to CSV.")
    
    def close(self):
        self.cursor.close()
        self.connection.close()

def main():
     
       
    e1=Employee()  
    e1.create_employee_table()  
    while True:
            print("\n1. Add Employee")
            print("2. Read Employees")
            print("3. Update employees Phone Numbers")
            print("4. Get Employees with Joining Year 2021 and Write to CSV")
            print("5. Exit")

            option = input("Select an option: ")

            if option == "1":
                print("Enter employee details:")
                employee_id = input("Employee Id: ")
                email = input("Email: ")
                name = input("Name: ")
                phone = input("Phone: ")
                pf_id = input("Pf Id: ")
                DOJ = input("Date of Joining:")
                DOB = input("Date of Birth: ")
                department = input("Department: ")
                e1.setter(employee_id,email,name,phone,pf_id,DOJ,DOB,department)
                e1.add()
            elif option == "2":
                e1.read()
            elif option == "3":
                e1.update()
            elif option == "4":
                e1.get_employees()
                e1.write_employees_to_csv()
            elif option == "5":
                break
            else:
                print("Invalid option. Please try again.")

    e1.close()

if __name__ == "__main__":
    main()