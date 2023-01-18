import os
import csv


total_months = 0
total_pc = 0
change = 0
greatest_increase = 0
increase_date = 0
greatest_decrease = 100000000000000
decrease_date = 0

# Open the CSV
with open("/Users/oliverzagorin/Desktop/GW_Bootcamp/Homework/python-challenge/PyBank/Resources/budget_data.csv") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)

    # Loop through updating variable values
    for row in csvreader:
        total_months += 1

        total_pc += int(row[1])
        if total_months > 1:
            change += int(row[1]) - previous_bl
       

            if int(row[1]) - previous_bl > greatest_increase:
                greatest_increase = int(row[1]) - previous_bl
                increase_date = (str(row[0]))
            
            if int(row[1]) - previous_bl < greatest_decrease:
                greatest_decrease = int(row[1]) - previous_bl
                decrease_date = (str(row[0]))

        previous_bl = int(row[1])

    output = (f"Financial Analysis\n"
  f"----------------------------\n"
        f"Total Months: {total_months}\n"
f"Total: ${total_pc}\n"
f"Average Change: ${round(change/(total_months-1),2)}\n"
f"Greatest Increase in Profits: {increase_date} (${greatest_increase})\n"
f"Greatest Decrease in Profits: {decrease_date} (${greatest_decrease})")

print(output)



with open("/Users/oliverzagorin/Desktop/GW_Bootcamp/Homework/python-challenge/PyBank/analysis/financial_analysis.txt", "w") as output_text:
    output_text.write(output)