import sys
import csv
import cs50

# check number of command-line arguments and remind user of usage if incorrect
if len(sys.argv) != 2:
    print("Usage: python import.py data.csv")
    sys.exit(1)

# get data file from command-line argument
data = sys.argv[1]

# connect to database
db = cs50.SQL("sqlite:///students.db")

# insert data into database
with open(data, "r") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:

        # parse names into first/last or first/middle/last according to number of spaces
        names = row["name"].split(" ")

        first = names[0]
        middle = None
        last = names[-1]

        if len(names) == 3:
            middle = names[1]

        # insert data, taking account of whether a middle name has been set
        if middle:
            db.execute("INSERT INTO students (first, middle, last, house, birth) VALUES(?, ?, ?, ?, ?)",
                       first, middle, last, row["house"], int(row["birth"]))
        else:
            db.execute("INSERT INTO students (first, last, house, birth) VALUES(?, ?, ?, ?)",
                       first, last, row["house"], int(row["birth"]))