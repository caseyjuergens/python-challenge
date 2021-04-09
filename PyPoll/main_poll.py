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
perc_votes = []

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

            # use append to add them to indiviual_candidates list and to the votes for candidates list
            individual_candidates.append(candidates)
            votes_for_candidates.append(1)

        # else, if that person is already in the individual candidates list
        else:

            #create and index of the individual candidates
            individual_candidates_index = individual_candidates.index(row[2])
            # add 1 vote to the individual
            votes_for_candidates[individual_candidates_index] += 1

            

           
            
    # percentage of votes each candidate won
    # find the winner 
for i in range(len(votes_for_candidates)):
    perc_votes.append(round((votes_for_candidates[i] / total_votes)*100)
    return str(perc_votes) + "%"

zipped_lists= zip(individual_candidates, votes_for_candidates, perc_votes)
zipped_lists= list(zipped_lists)

output= (
    f'Election Results\n'
    f'----------------------------\n'
    f'Total Votes: {total_votes} \n'
    f'----------------------------\n'
    f" {zipped_lists}\n"
    f'----------------------------\n'
    f'The winner is:'
    f'----------------------------\n'
)

#outside loop
print(output)
with open(file_output, "w") as txt_file:
    txt_file.write(output)
