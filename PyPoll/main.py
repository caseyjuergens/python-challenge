#import modules
import os
import csv

#establish file path
electdata = os.path.join("Resources", "election_data.csv")

#open file
with open(electdata) as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ",")
