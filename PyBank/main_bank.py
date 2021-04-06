# import module
import os
import csv

# establish path to resources folder/ budget data file
Pybank_csv = os.path.join("Resources", "budget_data.csv")
file_output = os.path.join("Analysis", "pybank_analysis.txt")

#global variables
total_months = 0
total_net = 0

#open and read budget data
with open(Pybank_csv) as csvfile:
    csvreader = csv.reader(csvfile)

    #ignore header
    header = next(csvreader)
    
    #loop thru rows in budgetdata
    for row in csvreader:
                                                                                      
        total_months +=1
        total_net= total_net + int(row[1])


output= (
    f'Financial Analysis\n'
    f'----------------------------\n'
    f'Total months: {total_months}\n'
    f'Net total: {total_net}\n'
    f'Average change: \n'
    f'Greatest Increase in Profit: \n'
    f'Greatest Decrease in Profit: \n'
)

    #outside loop
print(output)
with open(file_output, "w") as txt_file:
    txt_file.write(output)
