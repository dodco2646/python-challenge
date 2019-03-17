#pypoll business requirements
# 1. Open the .csv and set the delimiter
#2. Calculate 5 things:
#   1) total months included in the dataset
#   2)The net total amount of "Profit/Losses" over the entire period
#   3)The average of the changes in "Profit/Losses" over the entire period
#   4)The greatest increase in profits (date and amount) over the entire period
#   5)The greatest decrease in losses (date and amount) over the entire period
# Result should print to the terminal
# Result should export a .txt file with the results.

import csv
import os
import statistics
csvfile = "budget_data.csv"

#open and read the csv
with open(csvfile,newline="") as csvfile2:
    csvfinancials = csv.reader(csvfile2, delimiter=",")

    
    header = next(csvfinancials)
    monthlist  = []
    pandlsum = []
    pldelta = []
    V=0
    W=0

    for row in csvfinancials:
        monthlist.append(str(row[0]))
        pandlsum.append(int(row[1]))
    
    for value in pandlsum:
        if (int(value) - W) == int(value):
            pldelta.append(0)
            W = int(value)
            pldelta.pop(0)
        else:
            V = int(value) - W
            pldelta.append(V)
            W = value
  
    monthvaluedict ={}
    monthvaluedict["Months"] = monthlist
    monthvaluedict["Delta"] = pldelta

    PC=0
    for pchange in pldelta:
        if pchange > PC:
            PC = pchange

    

    NC=0
    for nchange in pldelta:
        if nchange < NC:
            NC = nchange



    
    csvandprint = str(f"Financiala Analysis\n----------------------------\
        \nTotal Months:{str(len(monthlist))}\
        \nTotal: ${sum(pandlsum)}\
        \nAverage Change:${statistics.mean(pldelta)}\
        \nGreatest Increase in Profits: ${int(PC)}\
        \nGreatest December in Profits: ${int(NC)}")

    print(csvandprint)
    textfile = open("FinancialResults.txt", "w")
    textfile.write(csvandprint)                         
