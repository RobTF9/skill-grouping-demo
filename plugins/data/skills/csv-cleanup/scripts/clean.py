import csv
import sys

for row in csv.reader(sys.stdin):
    print([cell.strip() for cell in row])
