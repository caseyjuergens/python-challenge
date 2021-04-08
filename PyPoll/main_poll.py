#import modules
import os
import csv

#establish file path
pypoll_csv = os.path.join("Resources", "election_data.csv")
file_output = os.path.join("Analysis", "pypoll_analysis.txt")

#global variables
total_votes = 0
# empty lists for candidates and their vote counts
individual_candidates = []
votes_for_candidates =[]

#open and read budget data
with open(pypoll_csv) as csvfile:
    csvreader = csv.reader(csvfile)

    #ignore header
    header = next(csvreader)
    
    #start loop
    for row in csvreader:
        #find total number of votes cast
        total_votes +=1

        # complete list of candidates
        candidates = row[2] 

        # if we come across a vote for a candidate who is not already in our individual list
        if candidates not in individual_candidates: 

            # use append to add them to indiviual_candidates 
            individual_candidates.append(candidates)

            # start counting votes for that individual candidate
            votes_for_candidates[individual_candidates] = 0

            # add 1 to votes_for_candidates
            
       

        # percentage of votes each candidate won


        # find the winner


output= (
    f'Election Results\n'
    f'----------------------------\n'
    f'Total Votes: {total_votes} \n'
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
