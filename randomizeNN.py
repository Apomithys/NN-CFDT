import random

import csv

with open(str(input("which file: ")), 'w') as file:
    thewriter = csv.writer(file)

    for o in range(0,100):
        row = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for i in range(0,9):
            row[i] = random.uniform(-1, 1)
        thewriter.writerow(row)
