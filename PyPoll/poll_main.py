import csv

P = open('/Users/oliverzagorin/Desktop/GW_Bootcamp/Homework/python-challenge/PyPoll/Resources/election_data.csv')

csv_P = csv.reader(P)
Poll_data = []

for row in csv_P:

    print(len(row))

P.close()
