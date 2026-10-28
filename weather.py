#read the weather csv file and display only weather record of ranchi city
import csv

with open('popular_cities_weather.csv', 'r') as file:
    csv_reader = csv.reader(file)

    for row in csv_reader:
        if row[-1] == 'Ranchi':  #only display the weather record of Ranchi city
            print(row)