import csv

while True:
    roll = int(input("Enter the roll number :"))
    name = input("Enter your name :")
    dept = input("Enter Department :")
    con  = input("Do you want to continue (y/n) :")

    if con.lower() == 'n':
        break

    with open('student.csv' , mode = 'a', newline = '') as file:
        
        writer = csv.writer(file)
        dataHeaders = ['roll','name','dept']
        data = [roll,name,dept]
        writer.writerow(dataHeaders)
        writer.writerow(data)
        print("Data submitted successfully")
   


