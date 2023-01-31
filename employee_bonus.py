import csv

EMPFILE = "EmployeePay.csv"


def main():
    infile = open(EMPFILE, "r", newline="")
    reader = csv.reader(infile)

    line = next(reader)

    print(
        format(line[0], "3"),
        format(line[1], "15"),
        format(line[2], "15"),
        format(line[3], "7"),
        format(line[4], "5"),
    )

    for line in reader:
        print(
            format(line[0], "3"),
            format(line[1], "15"),
            format(line[2], "15"),
            format(int(line[3]), "7,d"),
            format(float(line[4]), "5.0%"),
        )


main()
