import random
import csv

def randomizeNN():
    with open(str(input("which file: ")), 'w', newline='') as file:
        thewriter = csv.writer(file)
        howrow = int(input("how many rows: "))
        howcoul = int(input("how many columns: "))
        for o in range(0, howrow):
            row = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            for i in range(0, howcoul):
                row[i] = float(random.uniform(-0.1, 0.1))
            thewriter.writerow(row)

randomizeNN()