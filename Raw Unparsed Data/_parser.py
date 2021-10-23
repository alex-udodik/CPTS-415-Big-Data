import csv

with open('Accessories.csv', mode ='r') as file:
    csvFile = csv.reader(file)

 
    for lines in csvFile:
        print(lines)
        

