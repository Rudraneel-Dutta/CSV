import csv


dataHeaders = ['roll','name','dept']

with open('studentDict.csv' , mode = 'w', newline = '') as file:     
    writer = csv.DictWriter(file,fieldnames=dataHeaders)
    writer.writeheader()
    while True:
        roll = int(input("Enter the roll number :"))
        name = input("Enter your name :")
        dept = input("Enter Department :")           
        data = {'roll':roll,'name':name,'dept':dept}     
        writer.writerow(data)
        print("Data submitted successfully")
        con  = input("Do you want to continue (y/n) :")
        if con.lower() == 'n':
            break
        


