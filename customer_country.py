import csv

CUSTFILE = "customers.csv"
OUTFILE = "customer_country.csv"


def main():
    infile = open(CUSTFILE, "r", newline="")
    reader = csv.reader(infile)

    outfile = open(OUTFILE, "w", newline="")
    writer = csv.writer(outfile, delimiter=",")

    next(reader)
    writer.writerow(["FirstName", "LastName", "Country"])

    for line in reader:
        writer.writerow([line[1], line[2], line[4]])

    infile.close()
    outfile.close()


main()
