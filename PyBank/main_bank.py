# import module
import os
import csv

# establish path to resources folder/ budget data file
Pybank_csv = os.path.join("Resources", "budget_data.csv")

#create function with "budgetdata" as parameter
def PyBank_Totals(budget_data)
    #create variables
    month = str(Pybank_csv[0])
    ProfitLoss = int(Pybank_csv[1])

    #find total months included in data set
    total_months = len(month)
    print(total_months)

    #net total amount of profits/losses for entire period
    ProfitLoss = 0
    total_ProfitLoss += ProfitLoss
    print(total_ProfitLoss)
    
    #calculate changes in profits/losses for entire period/find average

    #find greatest increase in profits (date and amount) 

    #find greatest decrease in losees (date and amount)

#open and read budget data
with open(Pybank_csv) as csvfile:
    csvreader = csv.reader(csvfile)

    #ignore header
    header = next(csvreader)
    print(header)


#final script printing results, and export text file