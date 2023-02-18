import csv
from datetime import datetime
def readCSV():
    print("here1")
    file = open("Origin.csv" , 'r')
    file1 = open("Result.csv" , 'w', newline="")
    csvreader = csv.reader(file,delimiter=',',quotechar=',')
    csvwriter = csv.writer(file1)
    csvwriter.writerow((["year","region","value"]))
    next(csvreader, None)
    for rows in csvreader:
        print(rows)
        date_str = rows[0]
        date_obj = datetime.strptime(date_str, '%Y-%b')
        new_date_str = date_obj.strftime('%d-%m-%Y')
        rows[0] = new_date_str
        print(rows)
        csvwriter.writerow((rows[0], rows[1], rows[2]))

readCSV()