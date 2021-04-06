#import modules
import os
import csv

#establish file path
pypoll_csv = os.path.join("Resources", "election_data.csv")
file_output = os.path.join("Analysis", "pypoll_analysis.txt")

#global variables
total_votes = 0

#open and read budget data
with open(pypoll_csv) as csvfile:
    csvreader = csv.reader(csvfile)

    #ignore header
    header = next(csvreader)
    
    #start loop
    for row in csvreader:
        #find total number of votes cast
        total_votes +=1








output= (
    f'Election Results\n'
    f'----------------------------\n'
    f'Total Votes: \n'
    f'----------------------------\n'
    f'Khan: \n'
    f'Correy: \n'
    f'Li: \n'
    f"O'Tooley: \n"
    f'----------------------------\n'
    f'Winner: \n'
    f'----------------------------\n'
)

#outside loop
print(output)
with open(file_output, "w") as txt_file:
    txt_file.write(output)