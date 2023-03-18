import csv

ddmmyy = {
    "20200131": "01-31-2020",
    "20200231": "02-31-2020",
    "20200331": "03-31-2020",
    "20200431": "04-31-2020",
    "20200531": "05-31-2020",
    "20200631": "06-31-2020",
    "20200731": "07-31-2020",
    "20200831": "08-31-2020",
    "20200931": "09-31-2020",
    "20201031": "10-31-2020",
    "20201131": "11-31-2020",
    "20201231": "12-31-2020"
}
file = open("Orriginal.csv", 'r')
file2 = open("Resultat.csv", 'w', newline='')
csvreader = csv.reader(file,delimiter=',',quotechar=',')
csvwriter = csv.writer(file2)
csvwriter.writerow((["year","region","value"]))
next(csvreader, None)
next(csvreader, None)
for row in csvreader:
        row[0] = ddmmyy[row[0]]
        csvwriter.writerow(row)
