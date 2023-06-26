import csv
import mysql.connector

def insert_employees_from_csv(csv_file, host, database, user, password):
    conn = mysql.connector.connect(
        host=host,
        database=database,
        user=user,
        password=password
    )
    cursor = conn.cursor()

    # Create the Employees table if it doesn't exist
    cursor.execute('''CREATE TABLE IF NOT EXISTS Employees (
                        id INT PRIMARY KEY,
                        name VARCHAR(255),
                        department VARCHAR(255),
                        salary FLOAT
                    )''')
    conn.commit()

    # Read data from the CSV file and insert into the database
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        employees = []
        for row in reader:
            id = int(row['ID'])
            name = row['Name']
            department = row['Department']
            salary = float(row['Salary'])
            employees.append((id, name, department, salary))

        cursor.executemany('''INSERT INTO Employees (id, name, department, salary)
                              VALUES (%s, %s, %s, %s)''', employees)
        conn.commit()

    conn.close()
    print("Data inserted into the database successfully!")

# Specify the path to the CSV file and MySQL database credentials
csv_file_path = 'employees.csv'
host = 'SHTLP0145'
database = 'py_database'
user = 'root'
password = 'Chetna@1997'

# Call the function to insert employees from the CSV into the MySQL database
insert_employees_from_csv(csv_file_path, host, database, user, password)
