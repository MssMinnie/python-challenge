import os
import csv

csvpath = './election_data.csv'

vote_total = 0
vote_winner = 0
candidate_total = 0
most_votes = ["", 0]
candidates = []
cand_votes = {}


# Read in the CSV file
with open(csvpath, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
	
	# Read the header row
    #csv_header = next(csvreader)
    #election.append(csv_header)
    
    for row in csvreader:
        vote_total += 1
        candidate_total = row['Candidate']
        
        if row['Candidate'] not in candidates:
            candidates.append(row['Candidate'])
            cand_votes[row['Candidate']] = 1
            
        else:
            cand_votes[row['Candidate']] += 1
            
    for candidate in cand_votes:
        print(candidate + " " + str(round(((cand_votes[candidate]/votes)*100))) + "%" + " (" + str(candid_votes[candidate]) + ")") 
        candidate_total = (candidate + " " + str(round(((cand_votes[candidate]/votes)*100))) + "%" + " (" + str(cand_votes[candidate]) + ")")        
    
  
    print("Election Results/n" "---------------------")
    print(f"Total Votes: {vote_total}")