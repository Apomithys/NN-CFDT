import random
import csv

def randomizeNN(nameNN):
    with open(str(nameNN), 'w', newline='') as file:
        thewriter = csv.writer(file)
        print("start 'randomizeNN'")
        howrow = int(input("how many rows: "))
        howcoul = int(input("how many columns: "))
        for o in range(0, howrow):
            row = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            for i in range(0, howcoul):
                row[i] = float(random.uniform(-0.1, 0.1))
            thewriter.writerow(row)