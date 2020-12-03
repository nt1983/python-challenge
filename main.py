import csv
import os
filepath='Instructions\\PyBank\\Resources.budget_data.csv'
with open(filepath) as csvfile:
    csvreader=csv.reader(csvfile,delimiter=",")

    for row in csvreader:
        