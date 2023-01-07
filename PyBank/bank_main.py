import os
import csv

# Set path for file
csvpath = os.path.join("..", "Resources", "budget_data.csv")

total_months = 0
total_pc = 0
change = 0
greatest_increase = 0
increase_date = 0
greatest_decrease = 0
decrease_date = 0

# Open the CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Loop through updating variable values
    for row in csvreader:

        total_months == total_months +1

        total_pc == total_pc + int(row, 2)

        change == change + abs(int(row,2) - int(row-1,2))

        if (int(row,2) - int(row-1,2)) > greatest_increase:
            greatest_increase == (int(row,2) - int(row-1,2))
            increase_date == (str(row,1))
        
        elif (int(row,2) - int(row-1,2)) < greatest_decrease:
            greatest_decrease == (int(row,2) - int(row-1,2))
            decrease_date == (str(row,1))

    print(f"Total Months: {total_months}")
    print(f"Total: {total_pc}")
    print(f"Average Change: {change/total_months}")
    print(f"Greatest Increase in Profits: {increase_date} ({greatest_increase})")
    print(f"Greatest Increase in Profits: {decrease_date} ({greatest_decrease})")
    


    # If the book is never found, alert the user
