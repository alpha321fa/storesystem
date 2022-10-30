import sqlite3, random, datetime
from send_email import send_email
#The system connects to the database that will be used by the business.
#When the system is used for the first time, the tables will be created.
#The system will also fill the database with data that already exists within the business.
#The system uses a try and except statement to make sure that the database will not recreate the tables if they already exist.
connection = sqlite3.connect("DigitalFunhouse.db")
c = connection.cursor()
try:
    c.execute('''CREATE TABLE staff_table(staffID TEXT NOT NULL,
                                          FirstName TEXT,
                                          Surname TEXT,
                                          PhoneNumber TEXT,
                                          Email TEXT,
                                          HourlyRate FLOAT,
                                          HoursWorked INTEGER DEFAULT 0,
                                          Username TEXT,
                                          Password TEXT,
                                          Access TEXT,
                                          primary key(staffID))''')
    c.execute('''CREATE TABLE items_table(itemID TEXT NOT NULL,
                                          ItemName TEXT,
                                          Rentable BOOLEAN,
                                          Price FLOAT,
                                          RentalPrice FLOAT DEFAULT 0.0,
                                          RemainingStock INTEGER,
                                          ItemIncome FLOAT DEFAULT 0.0,
                                          NumberOfSales INTEGER DEFAULT 0,
                                          primary key(itemID))''')
    c.execute('''CREATE TABLE purchases_table(purchaseID TEXT NOT NULL,
                                          itemID TEXT NOT NULL,
                                          staffID TEXT NOT NULL,
                                          NumberOfDays INTEGER,
                                          PurchaseDate DATE,
                                          ReturnDate DATE,
                                          LateBill FLOAT DEFAULT 0.0,
                                          primary key(purchaseID),
                                          foreign key(itemID) REFERENCES items_table(itemID),
                                          foreign key(staffID) REFERENCES staff_table(staffID))''')
    c.execute('''CREATE TABLE customer_table(customerID INTEGER NOT NULL,
                                          FirstName TEXT,
                                          surname TEXT,
                                          PhoneNumber TEXT,
                                          Email TEXT,
                                          purchaseID TEXT NOT NULL,
                                          primary key(customerID),
                                          foreign key(purchaseID) REFERENCES purchases_table(purchaseID))''')
    c.execute('''CREATE TABLE orders_table(orderID TEXT NOT NULL,
                                          staffID TEXT NOT NULL,
                                          itemID TEXT NOT NULL,
                                          MinimumNumberForDelivery INTEGER,
                                          OrderCost FLOAT,
                                          NumberOfUnits INTEGER,
                                          OrdersMade INTEGER DEFAULT 0,
                                          primary key(orderID),
                                          foreign key(staffID) REFERENCES staff_table(staffID),
                                          foreign key(itemID) REFERENCES item_table(itemID))''')

#Inserting staff members into database
    c.execute('''INSERT INTO staff_table(staffID, FirstName, Surname, PhoneNumber, Email, HourlyRate, HoursWorked, Username, Password, Access)
    VALUES (11, 'Greg', 'Rees','07543976856', 'gregrees@gmail.com', 15.0, 0, 'grees11', 'testing1', 'Management')''')
    c.execute('''INSERT INTO staff_table(staffID, FirstName, Surname, PhoneNumber, Email, HourlyRate, HoursWorked, Username, Password, Access)
    VALUES (77, 'Hopper', 'Truth','07543976756', 'hoppertruth@gmail.com', 20.0, 0, 'htruth77', 'truth123', 'Management')''')
    c.execute('''INSERT INTO staff_table(staffID, FirstName, Surname, PhoneNumber, Email, HourlyRate, HoursWorked, Username, Password, Access)
    VALUES (44, 'Justin', 'Sain','07543976356', 'justinsain@gmail.com', 15.0, 0, 'jsain43', 'justin123', 'Management')''')
    c.execute('''INSERT INTO staff_table(staffID, FirstName, Surname, PhoneNumber, Email, HourlyRate, HoursWorked, Username, Password, Access)
    VALUES (13, 'Jon', 'Smith','07543956856', 'jonsmith@gmail.com', 14.0, 0, 'jsmith43', 'testing2', 'Finance')''')
    c.execute('''INSERT INTO staff_table(staffID, FirstName, Surname, PhoneNumber, Email, HourlyRate, HoursWorked, Username, Password, Access)
    VALUES (27, 'Marie', 'Jones','07583976856', 'mariejones@gmail.com', 14.0, 0, 'mjones27', 'marie123', 'Finance')''')
    c.execute('''INSERT INTO staff_table(staffID, FirstName, Surname, PhoneNumber, Email, HourlyRate, HoursWorked, Username, Password, Access)
    VALUES (89, 'Kate', 'Powell','07513976856', 'katepowell@gmail.com', 12.50, 0, 'kpowell89', 'testing3', 'Sales')''')
    c.execute('''INSERT INTO staff_table(staffID, FirstName, Surname, PhoneNumber, Email, HourlyRate, HoursWorked, Username, Password, Access)
    VALUES (39, 'Jane', 'Williams','07743976856', 'janewilliams@gmail.com', 12.50, 0, 'jwilliams39', 'jane1234', 'Sales')''')
    c.execute('''INSERT INTO staff_table(staffID, FirstName, Surname, PhoneNumber, Email, HourlyRate, HoursWorked, Username, Password, Access)
    VALUES (33, 'Sam', 'Carter','07543976896', 'samcarter@gmail.com', 12.50, 0, 'scarter33', 'carter123', 'Sales')''')

#Inserting items into database
    c.execute('''INSERT INTO items_table(itemID, ItemName, Rentable, Price, RentalPrice, RemainingStock, ItemIncome, NumberOfSales)
    VALUES (101, 'Call Of Duty: Cold War', TRUE, 50.0, 20.0, 120, 0.0, 0)''')
    c.execute('''INSERT INTO items_table(itemID, ItemName, Rentable, Price, RentalPrice, RemainingStock, ItemIncome, NumberOfSales)
    VALUES (333, 'Call Of Duty T-Shirt', FALSE, 20.0, 0, 50, 0.0, 0)''')
    c.execute('''INSERT INTO items_table(itemID, ItemName, Rentable, Price, RentalPrice, RemainingStock, ItemIncome, NumberOfSales)
    VALUES (955, 'PS5', FALSE, 450.0, 0.0, 40, 0.0, 0)''')
    c.execute('''INSERT INTO items_table(itemID, ItemName, Rentable, Price, RentalPrice, RemainingStock, ItemIncome, NumberOfSales)
    VALUES (456, 'Gaming Monitor', False, 120.0, 0.0, 80, 0.0, 0)''')
    c.execute('''INSERT INTO items_table(itemID, ItemName, Rentable, Price, RentalPrice, RemainingStock, ItemIncome, NumberOfSales)
    VALUES (543, 'Xbox One', False, 250.0, 0.0, 40, 0.0, 0)''')
    c.execute('''INSERT INTO items_table(itemID, ItemName, Rentable, Price, RentalPrice, RemainingStock, ItemIncome, NumberOfSales)
    VALUES (467, 'Playstation Code', FALSE, 50.0, 0.0, 80, 0.0, 0)''')
    c.execute('''INSERT INTO items_table(itemID, ItemName, Rentable, Price, RentalPrice, RemainingStock, ItemIncome, NumberOfSales)
    VALUES (555, 'Xbox Code', False, 50.0, 20.0, 80, 0.0, 0)''')
    c.execute('''INSERT INTO items_table(itemID, ItemName, Rentable, Price, RentalPrice, RemainingStock, ItemIncome, NumberOfSales)
    VALUES (789, 'Minecraft', TRUE, 25.0, 10.0, 120, 0.0, 0)''')
    c.execute('''INSERT INTO items_table(itemID, ItemName, Rentable, Price, RentalPrice, RemainingStock, ItemIncome, NumberOfSales)
    VALUES (788, 'Minecraft T-Shirt', False, 20.0, 0.0, 30, 0.0, 0)''')
    c.execute('''INSERT INTO items_table(itemID, ItemName, Rentable, Price, RentalPrice, RemainingStock, ItemIncome, NumberOfSales)
    VALUES (111, 'Grand Theft Auto V', TRUE, 30.0, 12.0, 70, 0.0, 0)''')
    c.execute('''INSERT INTO items_table(itemID, ItemName, Rentable, Price, RentalPrice, RemainingStock, ItemIncome, NumberOfSales)
    VALUES (123, 'FIFA 21', TRUE, 50.0, 20.0, 110, 0.0, 0)''')
    c.execute('''INSERT INTO items_table(itemID, ItemName, Rentable, Price, RentalPrice, RemainingStock, ItemIncome, NumberOfSales)
    VALUES (133, 'FIFA T-Shirt', FALSE, 20.0, 0.0, 40, 0.0, 0)''')
    c.execute('''INSERT INTO items_table(itemID, ItemName, Rentable, Price, RentalPrice, RemainingStock, ItemIncome, NumberOfSales)
    VALUES (145, 'Playstation Controller', FALSE, 50.0, 0.0, 60, 0.0, 0)''')
    c.execute('''INSERT INTO items_table(itemID, ItemName, Rentable, Price, RentalPrice, RemainingStock, ItemIncome, NumberOfSales)
    VALUES (154, 'Xbox Controller', FALSE, 50.0, 0.0, 70, 0.0, 0)''')
    c.execute('''INSERT INTO items_table(itemID, ItemName, Rentable, Price, RentalPrice, RemainingStock, ItemIncome, NumberOfSales)
    VALUES (777, 'Red Dead Redemption 2', TRUE, 35.0, 14.0, 30, 0.0, 0)''')
    c.execute('''INSERT INTO items_table(itemID, ItemName, Rentable, Price, RentalPrice, RemainingStock, ItemIncome, NumberOfSales)
    VALUES (177, 'Battlefield V', TRUE, 40.0, 16.0, 30, 0.0, 0)''')

#Inserting orders into database
    c.execute('''INSERT INTO orders_table(orderID, staffID, itemID, MinimumNumberForDelivery, OrderCost, NumberOfUnits, OrdersMade)
    VALUES ('B123', 11, 101, 15, 4000.0, 100, 0)''')
    c.execute('''INSERT INTO orders_table(orderID, staffID, itemID, MinimumNumberForDelivery, OrderCost, NumberOfUnits, OrdersMade)
    VALUES ('B124', 11, 333, 5, 400.0, 40, 0)''')
    c.execute('''INSERT INTO orders_table(orderID, staffID, itemID, MinimumNumberForDelivery, OrderCost, NumberOfUnits, OrdersMade)
    VALUES ('B125', 11, 955, 0, 4500.0, 10, 0)''')
    c.execute('''INSERT INTO orders_table(orderID, staffID, itemID, MinimumNumberForDelivery, OrderCost, NumberOfUnits, OrdersMade)
    VALUES ('B126', 44, 456, 10, 3000.0, 50, 0)''')
    c.execute('''INSERT INTO orders_table(orderID, staffID, itemID, MinimumNumberForDelivery, OrderCost, NumberOfUnits, OrdersMade)
    VALUES ('B127', 44, 543, 10, 6000.0, 40, 0)''')
    c.execute('''INSERT INTO orders_table(orderID, staffID, itemID, MinimumNumberForDelivery, OrderCost, NumberOfUnits, OrdersMade)
    VALUES ('B128', 77, 467, 20, 2000.0, 50, 0)''')
    c.execute('''INSERT INTO orders_table(orderID, staffID, itemID, MinimumNumberForDelivery, OrderCost, NumberOfUnits, OrdersMade)
    VALUES ('B129', 44, 555, 20, 2000.0, 50, 0)''')
    c.execute('''INSERT INTO orders_table(orderID, staffID, itemID, MinimumNumberForDelivery, OrderCost, NumberOfUnits, OrdersMade)
    VALUES ('B130', 77, 789, 15, 750.0, 50, 0)''')
    c.execute('''INSERT INTO orders_table(orderID, staffID, itemID, MinimumNumberForDelivery, OrderCost, NumberOfUnits, OrdersMade)
    VALUES ('B131', 11, 788, 5, 250.0, 25, 0)''')
    c.execute('''INSERT INTO orders_table(orderID, staffID, itemID, MinimumNumberForDelivery, OrderCost, NumberOfUnits, OrdersMade)
    VALUES ('B144', 11, 111, 15, 1000.0, 50, 0)''')
    c.execute('''INSERT INTO orders_table(orderID, staffID, itemID, MinimumNumberForDelivery, OrderCost, NumberOfUnits, OrdersMade)
    VALUES ('B166', 11, 123, 15, 1000.0, 50, 0)''')
    c.execute('''INSERT INTO orders_table(orderID, staffID, itemID, MinimumNumberForDelivery, OrderCost, NumberOfUnits, OrdersMade)
    VALUES ('B167', 44, 133, 5, 250.0, 25, 0)''')
    c.execute('''INSERT INTO orders_table(orderID, staffID, itemID, MinimumNumberForDelivery, OrderCost, NumberOfUnits, OrdersMade)
    VALUES ('B168', 77, 145, 10, 3200.0, 80, 0)''')
    c.execute('''INSERT INTO orders_table(orderID, staffID, itemID, MinimumNumberForDelivery, OrderCost, NumberOfUnits, OrdersMade)
    VALUES ('B196', 77, 154, 10, 3200.0, 80, 0)''')
    c.execute('''INSERT INTO orders_table(orderID, staffID, itemID, MinimumNumberForDelivery, OrderCost, NumberOfUnits, OrdersMade)
    VALUES ('B157', 44, 777, 15, 1250.0, 50, 0)''')
    c.execute('''INSERT INTO orders_table(orderID, staffID, itemID, MinimumNumberForDelivery, OrderCost, NumberOfUnits, OrdersMade)
    VALUES ('B137', 77, 177, 15, 1000.0, 40, 0)''')
    
    connection.commit()
except sqlite3.OperationalError:
    pass

#This function first displays a list of options that the staff members with access to sales menu will be able to use
#The first option allows the user to add customers to a database so that customer can be contacted with regards to their rental purchase
#And the staff member in charge of managing the customer will have access to the information about the purchase made by the customer
#The second option allows staff to change any customer details in the case where a customer has returned an item
#The third option allows staff to delete customers if customers know longer wish to keep their details to stay with the business
#The fourth option allows staff to create invoices for customers who have rented items and it is created by using a text file to store the invoice and using data from the database tables to generate the contents of the invoice
#The fifth option allows the staff to view customer details
#The sixth option allows the staff to see what items are available to be sold
#The seventh option allows the staff to confirm the purchase for a customer
#The eigth option allows a member of staff to add a rental purchase whenever a customer decides to a make a rental purchase
#The ninth option allows staff to edit a purchase a customer has made
#The tenth option allows staff to delete purchases which would usually be done after the customer has returned an item
#The eleventh option allows a staff member to input the number of hours that they have worked
#The twelfth option allows the staff member to exit the menu
#The code after the twelfth option checks the days remaining for a rental purchase made by a customer and it sends a reminder when there are seven days remaining
#The code also sends a reminder on the day that the customer has to return an item. The code uses then changes the values of the customers_checked variable to True so that the code isn't run again.
def sales_menu():
    customers_checked = False
    while True:
        print('''
Sales
1.  Add customer details
2.  Edit customer details
3.  Delete customer details
4.  Create and Send Invoice
5.  View customer details
6.  View Stock
7.  Confirm Purchase
8.  Add purchase
9.  Edit purchases
10. Delete purchases
11. Input Hours Worked
12. Exit''')
        #The user is asked to input the number next to the task that they want to complete
        option = int(input("Please enter the number that is next to the task that you want to do: "))
        if option == 1:
            #The system will keep on generating a customer ID until a customer ID that is not in the database is generated
            c.execute("SELECT customerID FROM customer_table")
            while True:
                customerID = random.randrange(1000,9999)
                if customerID not in c.fetchall():
                    break
            #The system checks whether there are any records in the purchases table
            c.execute("SELECT * FROM purchases_table")
            if c.fetchall():
                FirstName = input("Enter First Name: ")
                surname = input("Enter Surname: ")
                #The system checks whether the phone number is 11 numbers and it will ask the user to input the phone number again if it is not the correct length
                while True:
                    PhoneNumber = input("Enter Phone Number: ")
                    if len(PhoneNumber) > 11 or len(PhoneNumber) < 11:
                        break
                    else:
                        print("Phone number must be 11 numbers long.")
                #The system asks for the email and it makes sure that it is in the correct format
                while True:
                    Email = input("Enter Email: ")
                    if '@' in Email and ('.com' in Email or '.co.uk' in Email):
                        break
                    else:
                        print("Email is not in the correct format.")
                #The system prints all of the records in the purchases table so that the user can input the correct purchase ID
                c.execute("SELECT * FROM purchases_table")
                for row in c.fetchall():
                    print(row)
                c.execute("SELECT purchaseID FROM purchases_table")
                #The system will check whether the inputted purchase ID is in the database and it will insert the record into the database if it is in the database
                while True:
                    purchaseID = input("Enter Purchase ID: ")
                    for row in c.fetchall():
                        if purchaseID == row[0]:
                            c.execute("INSERT INTO customer_table (customerID, FirstName, surname, PhoneNumber, Email, purchaseID) VALUES (?,?,?,?,?,?)", (customerID, FirstName, surname, PhoneNumber, Email, purchaseID))
                            print("Customer added.")
                            connection.commit()
                            break
                    else:
                        print("Purchase ID must be in the purchase table.")
                    break
            else:
                print("Unable to add customer. You can only add customers after adding a purchase.")
        elif option == 2:
            #The system prints all records in the customer table so that the user can see which record to edit
            #If there are no records the system will tell the user that there is no records
            c.execute("SELECT * FROM customer_table")
            for row in c.fetchall():
                print(row)
            c.execute("SELECT * FROM customer_table")
            #The system will ask the user for record to edit, the new data to be inputted and the field that needs to be updated
            if c.fetchall():
                for row in c.fetchall():
                    print(row)
                try:
                    record = input("Please enter the customerID of the record that you want to update: ")
                    edit = input("Please enter the name of the field that you want to edit from the choices below:\nFirstName\nsurname\nPhoneNumber\nEmail\n ")
                    update = input("Please enter the new data: ")
                    c.execute("UPDATE customer_table SET "+edit+" = ? WHERE customerID = ?",(update, record))
                    print("Customer updated.")
                    connection.commit()
                except:
                    print("An error has ocurred when editing the database. Make sure that the data you enter is correct.")
            else:
                print("No customers to edit.")
        elif option == 3:
            #The system shows all records in the database and the system will ask the user which record that they want to delete
            c.execute("SELECT * FROM customer_table")
            if c.fetchall():
                c.execute("SELECT * FROM customer_table")
                for row in c.fetchall():
                    print(row)
                record = input("Please enter the customerID of the record that you want to delete: ")
                c.execute("DELETE FROM customer_table WHERE customerID = ?",(record,))
                print("Customer deleted.")
                connection.commit()
            else:
                print("No customers to delete.")
        elif option == 4:
            #The system will ask which customer that they want to send an invoice to and it will create an invoice using the customer's details from the database and the system will send it via email
            invoice = open('invoice.txt','w')
            customerID = int(input("Please enter the customer ID of the customer that you want to create an invoice for: "))
            c.execute("SELECT * FROM customer_table WHERE customerID = ?",(customerID,))
            customer = c.fetchone()
            c.execute("SELECT * FROM purchases_table WHERE purchaseID = ?",(customer[-1],))
            purchase = c.fetchone()
            c.execute("SELECT * FROM items_table WHERE itemID = ?",(purchase[1],))
            item = c.fetchone()
            invoice.writelines([datetime.date.today().strftime('%d/%m/%Y') + '\n', 'Digital Funhouse Invoice\n', customer[1] + ' ' + customer[2] + '\n', customer[3]+ '\n', customer[4]+ '\n',
                                'Item Name: '+item[1] + '\n', 'Price: '+str(item[4]) + '\n', 'Purchase Date: '+purchase[4] + '\n', 'Return Date: '+purchase[5] + '\n', 'Duration: '+str(purchase[3]) + '\n'])
            print("Invoice created.")
            invoice.close()
            try:
                send_email('digitalfunhouse@gmail.com', 'digitalfunhouse123', c.execute("SELECT Email FROM customer_table"), 'Your Digital Funhouse Rental Invoice', 'invoice.txt')
            except:
                print("Invoice sent.")
        elif option == 5:
            #The system prints all records in the database
            c.execute("SELECT * FROM customer_table")
            for row in c.fetchall():
                print(row)
        elif option == 6:
            #The system prints all records in the database
            c.execute("SELECT * FROM items_table")
            for row in c.fetchall():
                print(row)
        elif option == 7:
            #The system asks the user which item has been purchased and it decreases the value of the RemainingStock field by one.
            itemID = input("Enter the item ID of the item purchased: ")
            c.execute("UPDATE items_table SET RemainingStock = RemainingStock + 1 WHERE itemID = ?", (itemID,))
            print("Purchase Successful.")
            c.execute("SELECT RemainingStock FROM items_table WHERE itemID = ?", (itemID,))
            RemainingStock = c.fetchone()
            c.execute("SELECT MinimumNumberForDelivery FROM orders_table WHERE itemID = ?", (itemID,))
            Minimum = c.fetchone()
            #The system will then check whether the stock number has qualified for another delivery and it will send a reminder to the management staff
            if RemainingStock == Minimum:
                c.execute("SELECT ItemName FROM items_table WHERE itemID = ?", (itemID,))
                item_name = c.fetchone()
                item_reminder = open("item_reminder.txt", "w")
                item_reminder.write(item_name +" has reached the minimum number for delivery.")
                item_reminder.close()
                c.execute("SELECT staffID FROM orders_table WHERE itemID = ?", (itemID,))
                staffID = c.fetchone()
                c.execute("SELECT Email FROM staff_table WHERE staffID = ?", (staffID))
                email = c.fetchone()
                try:
                    send_email('digitalfunhouse@gmail.com', 'digitalfunhouse123', email, 'Item Reminder', 'item_reminder.txt')
                except:
                    print("Reminder Sent.")
        elif option == 8:
            #The system will keep on generating a purchase ID until a purchase ID that is not in the database is generated
            c.execute("SELECT purchaseID FROM purchases_table")
            while True:
                purchaseID = 'A' +str(random.randrange(1000,9999))
                if purchaseID not in c.fetchall():
                    break
            #The system prints all records in the items table so that the user can choose the correct item for the purchase
            c.execute("SELECT itemID, ItemName FROM items_table WHERE Rentable = TRUE")
            for row in c.fetchall():
                print(row)
            #The system will keep on asking for an item ID until the item ID entered is in the database
            while True:
                c.execute("SELECT itemID, ItemName FROM items_table")
                itemID = int(input("Please enter the item ID of the item bought: "))
                if itemID not in [ID[0] for ID in c.fetchall()]:
                    break
                else:
                    print("Item ID must be in items table.")
            #The user who is creating the purchase will enter their staff ID
            staffID = int(input("Please enter your staff ID: "))
            #The system will keep on asking the user to enter the return date until it is in the correct format
            while True:
                try:
                    PurchaseDate = datetime.date.today()
                    ReturnDate = input("Please enter the return date in the format YYYY-MM-DD: ")
                    datetime.date.fromisoformat(str(PurchaseDate))
                    datetime.date.fromisoformat(str(ReturnDate))
                    break
                except ValueError:
                    print("Invalid date format.")
            #The number of days that the item will be rented for is calculated and then the purchase is then inserted into the database
            NumberOfDays = (datetime.date.fromisoformat(str(ReturnDate)) - datetime.date.fromisoformat(str(PurchaseDate))).days
            c.execute("INSERT INTO purchases_table(purchaseID, itemID, staffID, NumberOfDays, PurchaseDate, ReturnDate) VALUES (?,?,?,?,?,?)",(purchaseID, itemID, staffID, NumberOfDays, PurchaseDate, ReturnDate))
            print("Purchase added.")
            connection.commit()
        elif option == 9:
            c.execute("SELECT * FROM purchases_table")
            for row in c.fetchall():
                print(row)
            try:
                record = input("Please enter the purchaseID of the record that you want to update: ")
                edit = input("Please enter the name of the field that you want to edit from the choices below:\nitemID\nstaffID\nPurchaseDate\nReturnDate\nNumberOfDays\n ")
                update = input("Please enter the new data: ")
                c.execute("UPDATE purchases_table SET "+edit+" = ? WHERE purchaseID = ?",(update, record))
                print("Purchase updated.")
                connection.commit()
            except:
                    print("An error has ocurred when editing the database. Make sure that the data you enter is correct.")
        elif option == 10:
            #The system shows all records in the database and the system will ask the user which record that they want to delete
            c.execute("SELECT * FROM purchases_table")
            for row in c.fetchall():
                print(row)
            record = input("Please enter the purchaseID of the record that you want to delete: ")
            c.execute("DELETE FROM purchases_table WHERE purchaseID = ?",(record,))
            print("Purchase deleted.")
            connection.commit()
        elif option == 11:
            #The system asks the user to enter their staff ID and to input the number of hours worked
            #The system adds the value inputted onto the value in the HoursWorked field
            staffID = input("Enter your staffID: ")
            c.execute("SELECT HoursWorked FROM staff_table WHERE staffID = ?", (staffID,))
            current_hours = c.fetchone()[0]
            new_hours = int(input("Enter the number of hours that you have worked: "))
            new_hours += current_hours
            c.execute("UPDATE staff_table SET HoursWorked = ? WHERE staffID = ?", (new_hours, staffID))
            connection.commit()
            print("Hours Updated.")
        elif option == 12:
            #Exits the menu
            break
        #The system runs the following code once to send reminders to customers
        c.execute("SELECT * FROM customer_table")
        if (not customers_checked) and c.fetchall():
            c.execute("SELECT purchaseID, NumberOfDays, itemID FROM purchases_table")
            #The system creates a reminder when the customer has seven days left to return their item
            for row in c.fetchall():
                if row[1] == 7:
                    reminder = open("reminder.txt", "w")
                    reminder.write("You have 7 days left to return your item.")
                    reminder.close()
                    c.execute("SELECT Email FROM customer_table WHERE purchaseID = ?", (row[0],))
                    email = c.fetchone()
                    try:
                        send_email('digitalfunhouse@gmail.com', 'digitalfunhouse123', email, 'Digital Funhouse Item Reminder', 'reminder.txt')
                    except:
                        print("Reminder Sent.")
                #The system sends a reminder and bills the customer when they have not returned their item
                #The late bill is calculated by taking 20 percent of the rental price
                elif row[1] == 0:
                    reminder = open("reminder.txt", "w")
                    reminder.write("You must return your item today or you will be charged the late fee.")
                    reminder.close()
                    c.execute("SELECT Email FROM customer_table WHERE purchaseID = ?", (row[0],))
                    email = c.fetchone()[0]
                    try:
                        send_email('digitalfunhouse@gmail.com', 'digitalfunhouse123', email, 'Digital Funhouse Item Reminder', 'reminder.txt')
                    except:
                        print("Reminder Sent.")
                    c.execute("SELECT RentalPrice FROM items_table WHERE itemID = ?", (row[2],))
                    late_fee = c.fetchone()[0] * 0.2
                    c.execute("UPDATE purchases_table SET LateBill = ? WHERE purchaseID = ?", (late_fee, row[0]))
                customers_checked = True

#This function first displays a list of options that the staff members with access to sales menu will be able to use
#The first option allows the finance staff to pay their employees and create a payslip to show details of the payment
#The second option allows staff to see how much money is being spent on what and how much money is being made
#The third otpion allows staff members to generate a report which consists of summary statistics about the popularity of items
#So that the management staff can make informed decisions regarding the items that they sell
#The fourth option allows finance staff to access the sales menu so that they can accomodate the customers and they can input their work hours
#The fifth option allows the staff member to exit the menu
def finance_menu():
    while True:
        print('''
Finance
1. Pay Employees
2. Manage expenses
3. Create Report
4. Access Sales
5. Exit''')
        #The user is asked to input the number next to the task that they want to complete
        option = int(input("Please enter the number that is next to the task that you want to do: "))
        if option == 1:
            #The system iterates through each staff member in the staff table and creates and sends a payslip to them
            #The pay is calculaed by multiplying the hours worked with the hourly rate.
            c.execute("SELECT FirstName, surname, HourlyRate, HoursWorked, Email FROM staff_table")
            for row in c.fetchall():
                print(row[0] + ' '+ row[1] +" has been paid "+ str(row[2]*row[3]))
                payslip = open("Payslip.txt", "w")
                payslip.writelines(["Digital Funhouse Payslip\n", datetime.date.today().strftime('%d/%m/%Y')+ '\n', row[0] + ' ' + row[1] + '\n', "Hours Worked: "+ str(row[2]) + '\n', "Hourly Rate: "+ str(row[3]) + '\n',
                                    "Total Earnings: "+ str(row[2]*row[3]) + '\n', "Tax Deductions: "+ str(row[2]*row[3]*0.2) + '\n', "Total Pay: "+ str(row[2]*row[3] - row[2]*row[3]*0.2) + '\n'])
                payslip.close()
                c.execute("UPDATE staff_table SET HoursWorked = 0 WHERE FirstName = ? AND surname = ?",(row[0], row[1]))
                try:
                    send_email('digitalfunhouse@gmail.com', 'digitalfunhouse123', row[4], 'Digital Funhouse Payslip', 'Payslip.txt')
                except:
                    print("Payslip sent to "+ row[0] +' '+ row[1])
        if option == 2:
            #The system fetches data from the databases to generate statistics about the expenses of the business
            order_costs = 0
            staff_costs = 0
            item_income = 0
            c.execute("SELECT OrderCost, OrdersMade FROM orders_table")
            for row in c.fetchall():
                order_costs += row[0]*row[1]
            c.execute("SELECT ItemIncome FROM items_table")
            for row in c.fetchall():
                item_income += row[0]
            c.execute("SELECT HourlyRate, HoursWorked FROM staff_table")
            for row in c.fetchall():
                staff_costs += (row[0]*row[1])
            print("Expenses\nOrder Costs: {0}\nStaff Costs: {0}\nIncome\nItem Income: {0}".format(order_costs, staff_costs, item_income))
        if option == 3:
            #The system creates a report using the item that has made the most money and the item that has made the least money
            report = open("Report.txt", "w")
            c.execute("SELECT MAX(NumberOfSales) FROM items_table")
            max_sales = c.fetchone()
            c.execute("SELECT ItemName FROM items_table WHERE NumberOfSales = ?", (max_sales))
            max_item = c.fetchone()
            max_report = "Best selling item is {0} with {1} units sold.".format(max_item, max_sales)
            c.execute("SELECT MIN(NumberOfSales) FROM items_table")
            min_sales = c.fetchone()
            c.execute("SELECT ItemName FROM items_table WHERE NumberOfSales = ?", (min_sales))
            min_item = c.fetchone()
            min_report = "Worst selling item is {0} with {1} units sold.".format(min_item, min_sales)
            report.writelines([max_report,'\n', min_report])
            report.close()
            #The report is then sent to each member of the management team
            for email in c.execute("SELECT Email FROM staff_table WHERE Access = 'Management'"):
                try:
                    send_email('digitalfunhouse@gmail.com', 'digitalfunhouse123', email, 'Digital Funhouse Report', 'Report.txt')
                except:
                    print("Report Sent.")
        if option == 4:
            #The system will access the function that contains the sales menu
            sales_menu()
        if option == 5:
            #Exits the menu
            break

#This function displays the a list of options available to the management staff
#The first 4 options allows management staff to add , edit, delete and view staff details
#The fifth and sixth options allows the management staff to access other departments and have access to the other options available
#The seventh, eight, ninth, and tenth options allows staff to add, edit, delete and view items that the business sells
#The four options before the last option allows staff to make deliveries for items as well as adding, editing and deleting order details from the databases
#The last option allows the staff member to exit the menu
def management_menu():
    while True:
        print('''
Management
1.  Add new staff
2.  Edit staff details
3.  Delete staff details
4.  View staff details
5.  Access Finance
6.  Access Sales
7.  Add new item
8.  Edit item details
9.  Delete item details
10. View item details
11. Order items
12. Add order details
13. Edit order details
14. Delete order details
15. Exit''')
        #The user is asked to input the number next to the task that they want to complete
        option = int(input("Please enter the number that is next to the task that you want to do: "))
        if option == 1:
            #The system will keep on generating a staff ID until a staff ID that is not in the database is generated
            c.execute("SELECT staffID from staff_table")
            while True:
                staffID = random.randrange(10,99)
                if staffID not in c.fetchall():
                    break
            #The system asks for the first name and surname of the staff member
                firstname = input("Enter First Name: ")
                surname = input("Enter Surname: ")
            #The system checks whether the phone number is 11 numbers and it will ask the user to input the phone number again if it is not the correct length
            while True:
                    PhoneNumber = input("Enter Phone Number: ")
                    if len(PhoneNumber) == 11:
                        break
                    else:
                        print("Phone number must be 11 numbers long.")
            #The system the asks for email, hourly rate and password and a username is generated by the system
            while True:
                    email = input("Enter Email: ")
                    if '@' in email and ('.com' in email or '.co.uk' in email):
                        break
                    else:
                        print("Email is not in the correct format.")
            HourlyRate = float(input("Please enter the employee's hourly rate: "))
            username = firstname[0] + surname + str(staffID)
            password = input("Please enter a new password: ")
            #The system will keep on asking for the access level until it is either 'Sales', 'Finance' or 'Management'
            while True:
                access = input("Please enter the employee's access level: ")
                if access.title() == 'Sales' or access.title() == 'Finance' or access.title() == 'Management':
                    break
                else:
                    print("Acess must be either Sales, Finance or Management.")
            #The record is then inserted into the database
            c.execute("INSERT INTO staff_table (staffID, FirstName, Surname, PhoneNumber, Email, HourlyRate, Username, Password, Access) VALUES (?,?,?,?,?,?,?,?,?)", (staffID, firstname, surname, PhoneNumber, email, HourlyRate, username, password, access.title()))
            print("Staff added.")
            connection.commit()
        if option == 2:
            #The system prints all records in the staff table so that the user can see which record to edit
            c.execute("SELECT * FROM staff_table")
            for row in c.fetchall():
                print(row)
            #The system will ask the user for record to edit, the new data to be inputted and the field that needs to be updated
            try:
                record = input("Please enter the staffID of the record that you want to update: ")
                edit = input("Please enter the name of the field that you want to edit from the choices below:\nFirstName\nSurname\nPhoneNumber\nEmail\nHourlyRate\nHoursWorked\nUsername\nPassword\nAccess\n")
                update = input("Please enter the new data: ")
                c.execute("UPDATE staff_table SET "+edit+" = ? WHERE staffID = ?",(update, record))
                print("Staff updated.")
                connection.commit()
            except:
                print("An error has ocurred when editing the database. Make sure that the data you enter is correct.")
        if option == 3:
            #The system shows all records in the database and the system will ask the user which record that they want to delete
            c.execute("SELECT * FROM staff_table")
            for row in c.fetchall():
                print(row)
            record = input("Please enter the staffID of the record that you want to delete: ")
            c.execute("DELETE FROM staff_table WHERE staffID = ?",(record,))
            print("Staff deleted.")
            connection.commit()
        if option == 4:
            #The system prints all records in the database
            c.execute("SELECT * FROM staff_table")
            for row in c.fetchall():
                print(row)
        if option == 5:
            #The system will access the function that contains the finance menu
            finance_menu()
        if option == 6:
            #The system will access the function that contains the sales menu
            sales_menu()
        if option == 7:
            #The system will keep on generating an item ID until an item ID that is not in the database is generated
            c.execute("SELECT itemID from items_table")
            while True:
                itemID = str(random.randrange(100,999))
                if itemID not in c.fetchall():
                    break
            #The system asks the user for the following information and the itemIncome and NumberOfSales variables are set to zero as a default value
            itemName = input("Please enter the name of the item: ")
            while True:
                Rentable = bool(input("Is the item rentable?(True/False): "))
                if str(Rentable) == 'True' or str(Rentable) == 'False':
                    break
                else:
                    print("Please enter True or False.")
            price = float(input("Please enter the standard price of the item: "))
            rentalPrice = float(input("Please enter the rental price of the item: "))
            RemainingStock = int(input("Please enter how many units of the item are available to be sold: "))
            itemIncome = 0
            NumberOfSales = 0
            #The record is then inserted into the database
            c.execute("INSERT INTO items_table VALUES (?,?,?,?,?,?,?,?)",(itemID, itemName, Rentable, price, rentalPrice, RemainingStock, itemIncome, NumberOfSales))
            print("Item added.")
            connection.commit()
        if option == 8:
            #The system prints all records in the staff table so that the user can see which record to edit
            c.execute("SELECT * FROM items_table")
            for row in c.fetchall():
                print(row)
            #The system will ask the user for record to edit, the new data to be inputted and the field that needs to be updated
            try:
                record = input("Please enter the itemID of the record that you want to update: ")
                edit = input("Please enter the name of the field that you want to edit from the choices below:\nitemName\nRentable\nPrice\nRentalPrice\nRemainingStock\nItemIncome\nNumberOfSales\n")
                update = input("Please enter the new data: ")
                c.execute("UPDATE items_table SET "+edit+" = ? WHERE itemID = ?",(update, record))
                print("Item updated.")
                connection.commit()
            except:
                print("An error has ocurred when editing the database. Make sure that the data you enter is correct.")
        if option == 9:
            #The system shows all records in the database and the system will ask the user which record that they want to delete
            c.execute("SELECT * FROM items_table")
            for row in c.fetchall():
                print(row)
            record = input("Please enter the itemID of the record that you want to delete: ")
            c.execute("DELETE FROM items_table WHERE itemID = ?",(record,))
            print("Item deleted.")
            connection.commit()
        if option == 10:
            #The system prints all records in the database
            c.execute("SELECT * FROM items_table")
            for row in c.fetchall():
                print(row)
        if option == 11:
            #The system prints all records in the database so that the user can see which order to make
            c.execute("SELECT * FROM orders_table")
            for row in c.fetchall():
                print(row)
            #The user inputs the order ID and then a delivery is made while the stock number in the database is updated and the OrdersMade field is increased by one
            orderID = input("Please enter the order ID of the order that you want to make: ")
            c.execute("SELECT itemID, NumberOfUnits, OrdersMade FROM orders_table WHERE orderID = ?", (orderID,))
            itemID, added_stock, OrdersMade = [data for data in c.fetchone()]
            c.execute("UPDATE items_table SET RemainingStock = RemainingStock + ? WHERE itemID = ?",(added_stock, itemID))
            c.execute("UPDATE orders_table SET OrdersMade = OrdersMade + 1 WHERE orderID = ?",(orderID,))
            print("Delivery Successful")
            connection.commit()
            #The system then creates an invoice for the business about the item that has is being delivered
            c.execute("SELECT OrderCost FROM orders_table WHERE orderID = ?", (orderID,))
            cost = c.fetchone()[0]
            business_invoice = open("business_invoice.txt", "w")
            business_invoice.writelines([datetime.date.today().strftime('%d/%m/%Y') + '\n', "Digital Funhouse Delivery Invoice\n", "Order ID: "+ orderID + '\n',
                                         "ItemID: "+ itemID + '\n', "Number Of Units: "+ str(added_stock) + '\n', "Delivery Cost: "+ str(cost) + '\n'])
            business_invoice.close()
            try:
                send_email('digitalfunhouse@gmail.com', 'digitalfunhouse123', c.execute("SELECT Email FROM staff_table WHERE staffID = (SELECT staffID FROM orders_table WHERE orderID = ?)",(orderID)), 'Digital Funhouse Order Invoice', 'business_invoice.txt')
            except:
                print("Invoice Sent.")
        if option == 12:
            #The system will keep on generating an order ID until an order ID that is not in the database is generated
            c.execute("SELECT orderID from orders_table")
            while True:
                orderID = 'B' +str(random.randrange(100,999))
                if orderID not in c.fetchall():
                    break
            #The system then asks the user for order details in the following lines and a record is then inserted into the database
            staffID = input("PLease enter the staff ID of the staff member responsible for making this delivery: ")
            itemID = input("Please enter the item ID of the item that will be delivered with this order: ")
            MinimumNumberForDelivery = int(input("Please enter the number that the item stock must fall below to qualify for a delivery: "))
            OrderCost = float(input("Please enter the cost of the order: "))
            NumberOfUnits = int(input("Please enter the number of units of the item that will be delivered: "))
            c.execute("INSERT INTO orders_table(orderID, staffID, itemID, MinimumNumberForDelivery, OrderCost, NumberOfUnits) VALUES (?,?,?,?,?,?)",(orderID, staffID, itemID, MinimumNumberForDelivery, OrderCost, NumberOfUnits))
            print("Order added.")
            connection.commit()
        if option == 13:
            #The system prints all records in the staff table so that the user can see which record to edit
            c.execute("SELECT * FROM orders_table")
            for row in c.fetchall():
                print(row)
            #The system will ask the user for record to edit, the new data to be inputted and the field that needs to be updated
            try:
                record = input("Please enter the orderID of the record that you want to update: ")
                edit = input("Please enter the name of the field that you want to edit from the choices:\norderID\nstaffID\nitemID\nMinimumNumberForDelivery\nOrderCost\nNumberOfUnits\n")
                update = input("Please enter the new data: ")
                c.execute("UPDATE orders_table SET "+edit+" = ? WHERE orderID = ?",(update, record))
                print("Order updated.")
                connection.commit()
            except:
                print("An error has ocurred when editing the database. Make sure that the data you enter is correct.")
        if option == 14:
            #The system shows all records in the database and the system will ask the user which record that they want to delete
            c.execute("SELECT * FROM orders_table")
            for row in c.fetchall():
                print(row)
            record = input("Please enter the orderID of the record that you want to delete: ")
            c.execute("DELETE FROM orders_table WHERE orderID = ?",(record,))
            print("Order deleted.")
            connection.commit()
        if option == 15:
            #Exits the menu
            break

#This is the interface that the user is greeted with when they start the system
#They are required to login by entering their username and password and what they have enetered will be checked in the databases to see if they match
#If the login is successful, the access level will be checked and they will be redirected to the menu that corresponds with their access level
while True:
    login = False
    while not login:
        c.execute("SELECT Username, Password FROM staff_table")
        username = input("Please enter your username: ")
        password = input("Please enter your password: ")
        for row in c.fetchall():
            if username == row[0] and password == row[1]:
                login = True
                break
        else:
            print("Incorrect Username or Password.")
            option = input("Do you wish to exit the sytsem. (Y/N)")
            if option.upper() == 'Y':
                connection.commit()
                connection.close()
                quit()
            else:
                pass
    if login:
        c.execute("SELECT Access FROM staff_table WHERE username = ? AND password = ?",(username, password))
        access = c.fetchone()[0]
        if access == 'Sales':
            sales_menu()
        elif access == 'Finance':
            finance_menu()
        elif access == 'Management':
            management_menu()
    option = input("Do you wish to exit the sytsem. (Y/N)")
    if option.upper() == 'Y':
        connection.commit()
        connection.close()
        quit()
    else:
        pass

