import csv

with open('../../tasks/Source/Source.csv', 'r') as input, open('../../tasks/Result/result.csv', 'w') as output:
    input_reader = csv.reader(input)
    output_writer = csv.writer(output)
    output_writer.writerow({"year","region","value"})
    next(input_reader, None)
    for row in input_reader:
        row[0]=row[0]+'-01-01'
        output_writer.writerow(row)
    print("completed")
