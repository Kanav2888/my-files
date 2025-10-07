import mysql.connector
from tabulate import tabulate   # optional pretty printing (install once: python -m pip install tabulate)

# Connect to MySQL
con = mysql.connector.connect(
    host="localhost",
    user="csproject",
    password="cs123",
    database="hospital"
)

cursor = con.cursor()

def add_patient():
    """Insert a new patient into the table"""
    name = input("Enter patient name: ")
    age = int(input("Enter age: "))
    gender = input("Enter gender: ")
    disease = input("Enter disease: ")

    sql = "INSERT INTO patients (name, age, gender, disease) VALUES (%s,%s,%s,%s)"
    cursor.execute(sql, (name, age, gender, disease))
    con.commit()
    print("Patient record added.\n")

def view_patients():
    """Fetch and display all patients"""
    cursor.execute("SELECT * FROM patients")
    rows = cursor.fetchall()
    if rows:
        print(tabulate(rows, headers=["Name", "Age", "Gender", "Disease"], tablefmt="grid"))
    else:
        print("No patient records found.\n")

def search_patient():
    """Search for patient by name"""
    name = input("Enter patient name to search: ")
    sql = "SELECT * FROM patients WHERE name=%s"
    cursor.execute(sql, (name,))
    rows = cursor.fetchall()
    if rows:
        print(tabulate(rows, headers=["Name", "Age", "Gender", "Disease"], tablefmt="grid"))
    else:
        print("No record found.\n")

def delete_patient():
    """Delete patient by name"""
    name = input("Enter patient name to delete: ")
    sql = "DELETE FROM patients WHERE name=%s"
    cursor.execute(sql, (name,))
    con.commit()
    print("Patient record deleted (if it existed).\n")

def menu():
    while True:
        print("\n=== Hospital Management System ===")
        print("1. Add Patient")
        print("2. View All Patients")
        print("3. Search Patient")
        print("4. Delete Patient")
        print("5. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            add_patient()
        elif choice == '2':
            view_patients()
        elif choice == '3':
            search_patient()
        elif choice == '4':
            delete_patient()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice.\n")

menu()

cursor.close()
con.close()
