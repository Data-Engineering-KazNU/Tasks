import csv

monthdict = {
    "Jan": "01-01",
    "Feb": "02-01",
    "Mar": "03-01",
    "Apr": "04-01",
    "May": "05-01",
    "Jun": "06-01",
    "Jul": "07-01",
    "Aug": "08-01",
    "Sep": "09-01",
    "Oct": "10-01",
    "Nov": "11-01",
    "Dec": "12-01"
}
with open('../../tasks/Source/Source2.csv', 'r') as source, open('../../tasks/Result/result2.csv', 'w') as output:
    input_reader = csv.reader(source)
    output_writer = csv.writer(output)
    output_writer.writerow(("year", "region", "value"))
    next(input_reader, None)
    for row in input_reader:
        row[0] = row[0][0:-3]+monthdict[row[0][5:8]]
        output_writer.writerow(row)
    print("completed")
