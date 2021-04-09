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
        #find number of total months                                                                              
        total_months +=1

        #find  net total of profit/losses of entire period
        total_net = total_net + int(row[1])

        #calculate the changes in prof/loss period, then find average
        average_change = total_net / total_months

        #find greatest increase/decrease in profits (dates and amounts)
        rows= list(csvreader)
        greatest_increase = max(rows, key=lambda row: int(row[1]))
        greatest_decrease = min(rows, key=lambda row: int(row[1]))
       
output=(
    f'Financial Analysis\n'
    f'----------------------------\n'
    f'Total months: {total_months}\n'
    f'Net total: ${total_net}\n'
    f'Average change: ${round(average_change)}\n'
    f'Greatest Increase in Profit: {greatest_increase}\n'
    f'Greatest Decrease in Profit: {greatest_decrease}\n'
)

#outside loop
print(output)
with open(file_output, "w") as txt_file:
    txt_file.write(output)