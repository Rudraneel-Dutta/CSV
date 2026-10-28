import csv

with open('student.csv', 'r') as file:
    csv_reader = csv.reader(file)

    for row in csv_reader:
        #print(row)
        #Show the roll number
        print(row[0])
