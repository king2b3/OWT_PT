"""
lower case everything
remove white space
how to check win?
if cell = blank
    cell = None

for key in master[key]
    if key = user[key]
        3 points
    elif detect correct win
        1 point
    else
        0 points
"""

from user import User
import csv

def exists(name) -> bool:
    """Checks if a user already exists in the database with that name"""
    ...

def read_data() -> dict:
    """Returns a dict with the match scores"""
    #Read csv
    #add values to list
    #Creates the master user
    ...


def main():
    week = 1
    #create master user with correct scores
    
    with open("weekly_data/week_1_pt.csv") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        #next(csv_reader)
        master = True
        for row in csv_reader:
            print(f"User {row['Discord Tag? **case sensitive**']}")
            if master:
                master_user = User(data=row,week=week)
                master = False
            else:

                temp = User(data=row,week=week)
                #print(row)
                temp == master_user
                temp.write()

if __name__ == '__main__':
    main()