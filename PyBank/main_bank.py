# import module
import os
import csv

# establish path to resources folder/ budget data file
Pybank_csv = os.path.join("Resources", "budget_data.csv")
 
#open and read budget data
with open(Pybank_csv) as csvfile:
    csvreader = csv.reader(csvfile)

    #ignore header
    header = next(csvreader)
    print(header)

   
