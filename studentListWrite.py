import csv

with open('student.csv' , mode = 'w', newline = '') as file:     
    writer = csv.writer(file)
    dataHeaders = ['roll','name','dept']
    writer.writerow(dataHeaders)

    while True:
        roll = int(input("Enter the roll number :"))
        name = input("Enter your name :")
        dept = input("Enter Department :")
        con  = input("Do you want to continue (y/n) :")    
        data = [roll,name,dept]     
        writer.writerow(data)
        print("Data submitted successfully")
        if con.lower() == 'n':
            break
    


