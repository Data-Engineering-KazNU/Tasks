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
with open('../../tasks/Source/Source3.csv', 'r') as source, open('../../tasks/Result/result3.csv', 'w', newline='') as output:
    input_reader = csv.reader(source)
    output_writer = csv.writer(output)
    output_writer.writerow(("year", "region", "value"))
    next(input_reader, None)
    for row in input_reader:
        row[0] = ddmmyy[row[0]]
        output_writer.writerow(row)
    print("completed")
