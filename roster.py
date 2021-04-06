# TODO
import sys
import cs50

# check number of command-line arguments and remind user of usage if incorrect
if len(sys.argv) != 2:
    print("Usage: python roster.py house")
    sys.exit(1)

# get house from command-line argument
house = sys.argv[1]

# connect to database
db = cs50.SQL("sqlite:///students.db")

# get student data for house
data = db.execute("SELECT * FROM students WHERE house = ? ORDER BY last, first", house)

# print student data, taking account of whether the student has a middle name
for student in data:
    if student['middle']:
        name = " ".join((student['first'], student['middle'], student['last']))
    else:
        name = " ".join((student['first'], student['last']))

    print(f"{name}, born {student['birth']}")