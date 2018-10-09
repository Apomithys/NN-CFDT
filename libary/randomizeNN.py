import random
import csv

def randomizeNN(nameNN, index):
    with open(str(nameNN), 'w', newline='') as file:
        thewriter = csv.writer(file)
        for o in range(0, index*10):
            row = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            for i in range(0, 10):
                row[i] = float(random.uniform(-float(1), float(1)))
            thewriter.writerow(row)
