import mysql.connector
import random

# Connect to MySQL
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Admin@123",
    database="hospital"
)
cur = con.cursor()

def add_patient():
    pid = random.randint(10000, 99999)
    name = input("Enter Patient Name: ")
    age = int(input("Enter Age: "))
    disease = input("Enter Disease: ")

    cur.execute("INSERT INTO patient (pid, name, age, disease) VALUES (%s, %s, %s, %s)",
                (pid, name, age, disease))
    con.commit()
    print(f"Patient Added Successfully! (Patient ID: {pid})\n")

def display_all():
    cur.execute("SELECT * FROM patient")
    result = cur.fetchall()

    print("\nPatient Records:")
    print(f"{'ID':<8}{'Name':<20}{'Age':<8}{'Disease':<15}")
    print("-" * 55)

    for row in result:
        print(f"{row[0]:<8}{row[1]:<20}{row[2]:<8}{row[3]:<15}")
    print()

def search_patient():
    pid = int(input("Enter Patient ID to Search: "))
    cur.execute("SELECT * FROM patient WHERE pid=%s", (pid,))
    result = cur.fetchone()
    if result:
        print("\nPatient Found:")
        print(f"ID: {result[0]}\nName: {result[1]}\nAge: {result[2]}\nDisease: {result[3]}\n")
    else:
        print("No Record Found.\n")

def update_patient():
    pid = int(input("Enter Patient ID to Update: "))
    disease = input("Enter New Disease: ")
    cur.execute("UPDATE patient SET disease=%s WHERE pid=%s", (disease, pid))
    con.commit()
    print("Record Updated!\n")

def delete_patient():
    pid = int(input("Enter Patient ID to Delete: "))
    cur.execute("DELETE FROM patient WHERE pid=%s", (pid,))
    con.commit()
    print("Record Deleted!\n")

while True:
    print('''
===== HOSPITAL MANAGEMENT SYSTEM =====
1. Add New Patient
2. Display All Patients
3. Search Patient
4. Update Patient
5. Delete Patient
6. Exit
''')
    choice = input("Enter your choice: ")

    if choice == '1':
        add_patient()
    elif choice == '2':
        display_all()
    elif choice == '3':
        search_patient()
    elif choice == '4':
        update_patient()
    elif choice == '5':
        delete_patient()
    elif choice == '6':
        print("Thank you for using the Hospital Management System!")
        break
    else:
        print("Invalid Choice! Try again.\n")
