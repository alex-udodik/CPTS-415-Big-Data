import csv

with open('Accessories.csv', mode ='r') as file:
    csvFile = csv.reader(file)

    count = 0
    for lines in csvFile:
        count = count + 1
    print(count)   

