import csv

INSALES = "sales.csv"
OUTSALES = "salesreport.csv"


def main():
    ifile = open(INSALES, "r", newline="")
    ofile = open(OUTSALES, "w", newline="")
    reader = csv.reader(ifile)
    writer = csv.writer(ofile, delimiter=",")

    next(reader)
    writer.writerow(["Customer, Total"])

    currCust = -1
    currTotal = 0

    for line in reader:
        if line[0] == currCust:
            currTotal += float(line[3]) + float(line[4]) + float(line[5])
        else:
            if currCust != -1:
                writer.writerow([currCust, round(currTotal, 2)])
            currCust = line[0]
            currTotal = float(line[3]) + float(line[4]) + float(line[5])


main()
