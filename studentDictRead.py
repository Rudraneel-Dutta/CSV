import csv
with open('student.csv','r') as file:
    csv_reader = csv.DictReader(file)

    for row in csv_reader:
        #print(row)
        #display the roll
        print(row['roll'])
