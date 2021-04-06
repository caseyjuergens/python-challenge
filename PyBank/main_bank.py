# import module
import os
import csv

# establish path to resources folder/ budget data file
Pybank_csv = os.path.join("Resources", "budget_data.csv")
file_output = os.path.join
#global variables
total_months = 0
total_net = 0

#open and read budget data
with open(Pybank_csv) as csvfile:
    csvreader = csv.reader(csvfile)

    #ignore header
    header = next(csvreader)
    
    
    for row in csvreader:
                                                                                      
        total_months +=1
        total_net= total_net + int(row[1])


output= (
    f'Financial analysis\n'
    f'-------------------\n'
    f'Total months is:{total_months}\n'
    f'Net total is: {total_net}\n'
    



)
    #outside loop
print(output)
with open(file_output, "w") as txt_file:
    txt_file.write(output)
  





    #final script printing results, and export text file
   # print(Print_totals)
