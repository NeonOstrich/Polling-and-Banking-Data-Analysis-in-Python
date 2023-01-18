import os
import csv

# Set path for file

total_votes = 0
candidate_list = []
candidate_dictionary = {}
percentage_dice = {}

# Open the CSV
with open("/Users/oliverzagorin/Desktop/GW_Bootcamp/Homework/python-challenge/PyPoll/Resources/election_data.csv") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    header = next(csvreader)

    # Loop through updating variable values
    for row in csvreader:

        total_votes += 1

        candidate_name = row[2]
        if candidate_name not in candidate_list:
            candidate_list.append(candidate_name)
            candidate_dictionary[candidate_name] = 0

        candidate_dictionary[candidate_name] +=1

    percentage_dict = {key: round((value / total_votes)*100,2) for key, value in candidate_dictionary.items()}

    max_dict = max(candidate_dictionary, key=candidate_dictionary.get)
    
    

    output = (f"Election Results\n"
    f"-------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"The candidates running are {candidate_list}\n"
        f"Total votes by candidate {candidate_dictionary}\n"
        f"Percentage votes by candidate {(percentage_dict)}\n"
        f"The winner is {max_dict}")

print(output)


with open("/Users/oliverzagorin/Desktop/GW_Bootcamp/Homework/python-challenge/PyPoll/analysis/financial_analysis.txt", "w") as output_text:
    output_text.write(output)