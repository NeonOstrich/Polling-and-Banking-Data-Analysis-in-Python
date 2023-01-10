import os
import csv

# Set path for file
csvpath = os.path.join("Resources", "election_data.csv")

total_votes = 0
candidate_list = []
candidate_dictionary = {}


# Open the CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    header = next(csvreader)

    # Loop through updating variable values
    for row in csvreader:

        total_votes = total_votes +1

        candidate_name = row[2]
        if candidate_name not in candidate_list:
            candidate_list.append(candidate_name)
            candidate_dictionary[candidate_name] = 0

        candidate_dictionary[candidate_name] +=1

    percentage_dict = {key: value / total_votes for key, value in candidate_dictionary.items()}


    print(f"Total Votes: {total_votes}")
    print(f"{candidate_list}")
    print(f"Average Change: {candidate_dictionary}")
    print(percentage_dict)
