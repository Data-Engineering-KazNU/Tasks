import csv
with open(r"C:\Users\USER\Desktop\Data\tasks\Task\hi.csv", "r") as fp, open (r"C:\Users\USER\Desktop\Data\tasks\Task\hi2.csv", "w", newline="") as wf:
    reader = csv.reader(fp, delimiter=",")
    writer = csv.writer(wf)
    next(reader,None)
    writer.writerow(("year","region", "value"))
    for row in reader:
        print(row[0]+"-01-01")
        writer.writerow((row[0]+"-01-01", row[1], row[2]))


