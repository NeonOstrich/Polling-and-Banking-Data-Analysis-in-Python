import os
import csv

# Set path for file
csvpath = os.path.join("..", "Resources", "election_data.csv")

total_votes = 0
candidate_list = []


# Open the CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Loop through updating variable values
    for row in csvreader:

        total_votes == total_votes +1




    print(f"Total Votes: int{total_votes}")
    print(f"str{candidate_list}")
    print(f"Average Change: {change/total_months}")
    print(f"Greatest Increase in Profits: {increase_date} ({greatest_increase})")
    print(f"Greatest Increase in Profits: {decrease_date} ({greatest_decrease})")
