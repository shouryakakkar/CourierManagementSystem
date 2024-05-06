
import mysql.connector

db = mysql.connector.connect(host='localhost', user='root', passwd='shourya')
cursor = db.cursor()
sql = ("Create database CSM")
cursor.execute(sql)
print("Database Created!")
import mysql.connector
db = mysql.connector.connect(host='localhost', user='root', passwd='shourya', database='CSM')
cursor = db.cursor()
cursor.execute("Create Table CustDetails(BookingID int(10) primary key, Name varchar(20), Phone int, Email varchar(80), Address varchar(200))")
cursor.execute("Create Table Staff(EmpID int primary key, EmpName varchar(20), Designation char(20), Joining_Date date, Salary int)")
cursor.execute("create table Shipment(BookingID int primary key, Book_Date date, Delivery_Date date, Origin varchar(80), Destination varchar(80))")
cursor.execute("Create Table Package(BookingID int primary key, Weight varchar(20), Items varchar(80), Contents varchar(80), Service_Type char(20))")
cursor.execute("create table Billing(BookingID int primary key, Name varchar(20), Charges varchar(20),Delivery_Type varchar(20), Payment_Mode varchar(20))")
print("Tables Created!")

print("-------------- COURIER SERVICE MANAGEMENT SYSTEM ----------------")
print("-------------------- DATABASE 2023 EDITION ----------------------")
print("----------- MADE BY: DREAMCATCHERS (SHOURYA KAKKAR) -------------")


a= input("Enter your password to continue: ")
print("\n")


if a!= 'shourya':
    print("Incorrect Password! Try again.")
    print("-------------------------------------------------------------")
elif a== 'shourya':
    def menu():
        c='y'
        while (c=='y'):
            print("1. Continue to Tables ")
            print("2. Quit")

            choice=int(input("Enter your choice: "))

            if choice == 1:
                Continue()

            elif choice == 2:
                print("Exiting. Have a nice day!")
                print("-------------------------------------------------")
                break

    c = input("Do you want to continue or not?: ")
    print("\n")



    def Continue():
        def menu():
            c='y'
            while (c=='y'):
                print("1. Make changes in table CustDetails")
                print("2. Make changes in table Staff")
                print("3. Make changes in table Shipment")
                print("4. Make changes in table Package")
                print("5. Make changes in table Billing")
                print("6. Exit")

                choice=int(input("Enter your choice: "))

                if choice == 1:
                    CustDetails()
                elif choice == 2:
                    Staff()
                elif choice == 3:
                    Shipment()
                elif choice == 4:
                    Package()
                elif choice == 5:
                    Billing()
                elif choice == 6:
                    print("Exiting! Have a nice day!")
                    print("---------------------------------------------")
                    break

                else:
                    print("Wrong Input!")
                    print("---------------------------------------------")

        c = input("Do you want to continue or not?: ")        

        def CustDetails():
            def menu():
                c='y'
                while (c=='y'):
                    print("1. Add record")
                    print("2. Update record")
                    print("3. Delete record")
                    print("4. Display record")
                    print("5. Exit")
                    choice=int(input("Enter your choice: "))
                    if choice == 1:
                        adddata()
                    elif choice == 2:
                        updatedata()
                    elif choice == 3:
                        deldata()
                    elif choice == 4:
                        fetchdata()
                    elif choice == 5:
                        print("Exiting. Have a nice day!")
                        print("-----------------------------------------")
                        break
                else:
                    print("Wrong Input!")
                    print("---------------------------------------------")
            c = input("Do you want to continue or not?: ")

            def adddata():
                import mysql.connector
                db = mysql.connector.connect(host='localhost', user='root',passwd='shourya', database='CSM')
                mycursor = db.cursor()
                A = int(input("Enter Booking ID : "))
                B = input("Enter Customer Name : ")
                C = input("Enter Phone Number : ")
                D = input("Enter Email : ")
                E = input("Enter Address : ")
                sql = ("INSERT INTO CustDetails VALUES(%s,%s,%s,%s,%s);")
                data=(A,B,C,D,E)
                mycursor.execute(sql,data)
                db.commit()
                mycursor.close()
                print("Records Added!")
                print("-------------------------------------------------")

            def updatedata():
                import mysql.connector
                db = mysql.connector.connect(host='localhost', user='root',passwd='shourya', database='CSM')
                cursor=db.cursor()
                BookingID =input("Enter Booking ID: ")
                query=('select * from CustDetails where BookingID=%s;')
                rec_srch=(BookingID,)
                Name = input("Enter updated name: ")
                Phone = input("Enter updated phone number: ")
                Email = input("Enter updated email: ")
                Address = input("Enter updated Address: ")
                qry = ("update CustDetails set Name=%s, Phone=%s, Email=%s, Address=%s where BookingID=%s;")
                data = (Name, Phone, Email, Address, BookingID)
                cursor.execute(qry,data)
                print("Record Updated!")
                print("-------------------------------------------------")
                db.commit()

            def deldata():
                import mysql.connector
                db = mysql.connector.connect(host='localhost', user='root', passwd='shourya', database='CSM')
                cursor=db.cursor()
                BookingID=input("Enter Booking ID: ")
                qry=("delete from CustDetails where BookingID=%s;")
                delete=(BookingID,)
                cursor.execute(qry,delete)
                db.commit()
                print("Record Deleted!")
                print("-------------------------------------------------")

            def fetchdata():
                import mysql.connector
                try:
                    db = mysql.connector.connect(host='localhost', user='root',passwd='shourya', database='CSM')
                    cursor=db.cursor()
                    cursor.execute("select * from CustDetails;")
                    results=cursor.fetchall()
                    for x in results:
                        print(x)
                except:
                     print("Error!")
                     print("--------------------------------------------")
            menu()

        def Staff():
            def menu():
                c='y'
                while (c=='y'):
                    print("1. Add record")
                    print("2. Update record")
                    print("3. Delete record")
                    print("4. Display record")
                    print("5. Exit")
                    choice=int(input("Enter your choice: "))
                    if choice == 1:
                        adddata()
                    elif choice == 2:
                        updatedata()
                    elif choice == 3:
                        deldata()
                    elif choice == 4:
                        fetchdata()
                    elif choice == 5:
                        print("Exiting. Have a nice day!")
                        break
                else:
                    print("Wrong Input!")
                    print("---------------------------------------------")
            c = input("Do you want to continue or not?: ")

            def adddata():
                import mysql.connector
                db = mysql.connector.connect(host='localhost', user='root', passwd='shourya', database='CSM')
                mycursor = db.cursor()
                A = int(input("Enter Employee ID : "))
                B = input("Enter Employee Name: ")
                C = input("Enter Designation : ")
                D = input("Enter Joining Date : ")
                E = int(input("Enter Salary : "))
                sql = ("INSERT INTO Staff VALUES(%s,%s,%s,%s,%s);")
                data=(A,B,C,D,E)
                mycursor.execute(sql,data)
                db.commit()
                mycursor.close()
                print("Records Added!")
                print("-------------------------------------------------")

            def updatedata():
                import mysql.connector
                db = mysql.connector.connect(host='localhost', user='root', passwd='shourya', database='CSM' )
                cursor=db.cursor()
                EmpID=input("Enter Employee ID: ")
                query=('select * from Staff where EmployeeID=%s;')
                rec_srch=(EmpID,)
                EmpName = input("Enter updated name: ")
                Designation = input("Enter updated designation: ")
                Joining_Date = input("Enter updated joining date: ")
                Salary = input("Enter updated salary:")
                qry=("update staff set EmpName=%s, Designation=%s, Joining_Date=%s, Salary=%s where EmpID=%s;")
                data = (EmpName, Designation, Joining_Date, Salary, EmpID)
                cursor.execute(qry,data)
                print("Record Updated!")
                print("-------------------------------------------------")
                db.commit()

            def deldata():
                import mysql.connector
                db = mysql.connector.connect(host='localhost', user='root', passwd='shourya', database='CSM')
                cursor=db.cursor()
                EmpID=input("Enter Employee ID: ")
                qry=("delete from Staff where EmpID=%s;")
                delete=(EmpID,)
                cursor.execute(qry,delete)
                db.commit()
                print("Record Deleted!")
                print("-------------------------------------------------")

            def fetchdata():
                import mysql.connector
                try:
                    db = mysql.connector.connect(host='localhost', user='root', passwd='shourya', database='CSM' )
                    cursor = db.cursor()
                    cursor.execute("select * from Staff;")
                    results = cursor.fetchall()
                    for x in results:
                        print(x)
                except:
                     print("Error!")
                     print("--------------------------------------------")
            menu()

        def Billing():
            def menu():
                c='y'
                while (c=='y'):
                    print("1. Add record")
                    print("2. Update record")
                    print("3. Delete record")
                    print("4. Display record")
                    print("5. Exit")
                    choice=int(input("Enter your choice: "))
                    if choice == 1:
                        adddata()
                    elif choice == 2:
                        updatedata()
                    elif choice == 3:
                        deldata()
                    elif choice == 4:
                        fetchdata()
                    elif choice == 5:
                        print("Exiting. Have a nice day!")
                        break
                else:
                    print("Wrong Input!")
                    print("---------------------------------------------")
            c = input("Do you want to continue or not?: ")

            def adddata():
                import mysql.connector
                db = mysql.connector.connect(host='localhost', user='root', passwd='shourya', database='CSM')
                mycursor = db.cursor()
                A = int(input("Enter Booking ID: "))
                B = input("Enter Name: ")
                C = int(input("Enter Charges: "))
                D = input("Enter Delivery Type: ")
                E = input("Enter Payment Mode: ")
                sql = ("INSERT INTO Billing VALUES(%s,%s,%s,%s,%s);")
                data=(A,B,C,D,E)
                mycursor.execute(sql,data)
                db.commit()
                mycursor.close()
                print("Records Added!")
                print("-------------------------------------------------")

            def updatedata():
                import mysql.connector
                db = mysql.connector.connect(host='localhost', user='root', passwd='shourya', database='CSM' )
                cursor=db.cursor()
                BookingID=input("Enter Booking ID: ")
                query=('select * from Billing where BookingID=%s;')
                rec_srch=(BookingID,)
                Name = input("Enter updated name: ")
                Charges = input("Enter updated charges: ")
                Delivery_Type = input("Enter updated delivery type: ")
                Payment_Mode = input("enter updated payment mode:")
                qry=("update Billing set Name=%s, Charges=%s, Delivery_Type=%s, Payment_Mode=%s where BookingID=%s;")
                data = (Name, Charges, Delivery_Type, Payment_Mode, BookingID)
                cursor.execute(qry,data)
                print("Record Updated!")
                print("-------------------------------------------------")
                db.commit()

            def deldata():
                import mysql.connector
                db = mysql.connector.connect(host='localhost', user='root',passwd='shourya', database='CSM' )
                cursor=db.cursor()
                BookingID=input("Enter BookingID: ")
                qry=("Delete from Billing where BookingID=%s;")
                delete=(BookingID,)
                cursor.execute(qry,delete)
                db.commit()
                print("Record Deleted!")
                print("-------------------------------------------------")
            def fetchdata():
                import mysql.connector
                try:
                    db = mysql.connector.connect(host='localhost', user='root', passwd='shourya', database='CSM')
                    cursor=db.cursor()
                    cursor.execute("select * from Billing;")
                    results=cursor.fetchall()
                    for x in results:
                        print(x)
                        print("-----------------------------------------")
                except:
                     print("Error!")
                     print("--------------------------------------------")
            menu()

        def Shipment():
            def menu():
                c='y'
                while (c=='y'):
                    print("1. Add record")
                    print("2. Update record")
                    print("3. Delete record")
                    print("4. Display record")
                    print("5. Exit")
                    choice=int(input("Enter your choice: "))
                    if choice == 1:
                        adddata()
                    elif choice == 2:
                        updatedata()
                    elif choice == 3:
                        deldata()
                    elif choice == 4:
                        fetchdata()
                    elif choice == 5:
                        print("Exiting. Have a nice day!")
                        break
                else:
                    print("Wrong Input!")
                    print("---------------------------------------------")
            c = input("Do you want to continue or not?: ")

            def adddata():
                import mysql.connector
                db = mysql.connector.connect(host='localhost', user='root', passwd='shourya', database='CSM')
                mycursor = db.cursor()
                A = int(input("Enter Booking ID: "))
                B = input("Enter Booking Date: ")
                C = input("Enter Delivery Date : ")
                D = input("Enter Origin: ")
                E = input("Enter Destination: ")
                sql = ("INSERT INTO Shipment VALUES(%s,%s,%s,%s,%s);")
                data=(A,B,C,D,E)
                mycursor.execute(sql,data)
                db.commit()
                mycursor.close()
                print("Records Added!")
                print("-------------------------------------------------")

            def updatedata():
                import mysql.connector
                db = mysql.connector.connect(host='localhost', user='root', passwd='shourya', database='CSM' )
                cursor=db.cursor()
                BookingID =  input("Enter Booking ID:")
                query=('select * from Shipment where BookingID=%s;')
                rec_srch=(BookingID,)
                Book_Date = input("Enter updated Booking Date: ")
                Delivery_Date = input("Enter updated Delivery Date:  ")
                Origin = input("Enter updated Origin: ")
                Destination = input("enter updated Destination:")
                qry=("update Shipment set Book_Date=%s, Delivery_Date=%s, Origin=%s,Destination=%s where BookingID=%s;")
                data = (Book_Date, Delivery_Date, Origin, Destination, BookingID)
                cursor.execute(qry,data)
                print("Record Updated!")
                print("-------------------------------------------------")
                db.commit()

            def deldata():
                import mysql.connector
                db = mysql.connector.connect(host='localhost', user='root', passwd='shourya', database='CSM' )
                cursor=db.cursor()
                BookingID=input("Enter Booking ID:")
                qry=("Delete from Shipment where BookingID=%s;")
                delete=(BookingID,)
                cursor.execute(qry,delete)
                db.commit()
                print("Record Deleted!")
                print("-------------------------------------------------")

            def fetchdata():
                import mysql.connector
                try:
                    db = mysql.connector.connect(host='localhost', user='root', passwd='shourya', database='CSM' )
                    cursor=db.cursor()
                    cursor.execute("select * from Shipment;")
                    results=cursor.fetchall()
                    for x in results:
                        print(x)
                        print("-----------------------------------------")
                except:
                     print("Error!")
                     print("--------------------------------------------")
            menu()

        def Package():
            def menu():
                c='y'
                while (c=='y'):
                    print("1. Add record")
                    print("2. Update record")
                    print("3. Delete record")
                    print("4. Display record")
                    print("5. Exit")
                    choice=int(input("Enter your choice: "))
                    if choice == 1:
                        adddata()
                    elif choice == 2:
                        updatedata()
                    elif choice == 3:
                        deldata()
                    elif choice == 4:
                        fetchdata()
                    elif choice == 5:
                        print("Exiting. Have a nice day!")
                        break
                else:
                    print("Wrong Input")
                    print("---------------------------------------------")
            c = input("Do you want to continue or not?: ")

            def adddata():
                import mysql.connector
                db = mysql.connector.connect(host='localhost', user='root', passwd='shourya', database='CSM')
                mycursor = db.cursor()
                A = int(input("Enter Booking ID: "))
                B = input("Enter Package Weight: ")
                C = int(input("Enter Number of Items: "))
                D = input("Enter Package Contents: ")
                E = input("Enter Service Type: ")
                sql = ("INSERT INTO Package VALUES(%s,%s,%s,%s,%s);")
                data=(A,B,C,D,E)
                mycursor.execute(sql,data)
                db.commit()
                mycursor.close()
                print("Records Added!")
                print("-------------------------------------------------")

            def updatedata():
                import mysql.connector
                db = mysql.connector.connect(host='localhost', user='root', passwd='shourya', database='CSM' )
                cursor=db.cursor()
                BookingID =input("Enter Booking ID: ")
                query=('select * from Package where BookingID=%s;')
                rec_srch=(BookingID,)
                Weight = input("Enter updated weight: ")
                Items = input("Enter updated number of items: ")
                Contents = input("Enter updated contents: ")
                Service_Type = input("Enter updated service type: ")
                qry = ("update Package set Weight=%s, Items=%s, Contents=%s, Service_Type=%s where BookingID=%s;")
                data =(Weight, Items, Contents, Service_Type, BookingID)
                cursor.execute(qry,data)
                print("Record Updated!")
                print("-------------------------------------------------")
                db.commit()

            def deldata():
                import mysql.connector
                db = mysql.connector.connect(host='localhost', user='root', passwd='shourya', database='CSM' )
                cursor=db.cursor()
                BookingID=input("Enter Booking ID:")
                qry=("delete from Package where BookingID=%s;")
                delete=(BookingID,)
                cursor.execute(qry,delete)
                db.commit()
                print("Record Deleted!")
                print("-------------------------------------------------")

            def fetchdata():
                import mysql.connector
                try:
                    db = mysql.connector.connect(host='localhost', user='root', passwd='shourya', database='CSM' )
                    cursor=db.cursor()
                    cursor.execute("select * from Package;")
                    results = cursor.fetchall()
                    for x in results:
                        print(x)
                except:
                     print("Error!")
                     print("--------------------------------------------")                
            menu() 
        menu()    
    menu()
cursor.execute("drop database CSM")
