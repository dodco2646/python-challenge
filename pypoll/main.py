# The total number of votes cast
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote.

import csv
import os
import statistics
csvfile = ("election_data.csv")

with open(csvfile,newline="") as csvfile2:
    csvelections = csv.reader(csvfile2, delimiter=",")

    header = next(csvelections)
    candidates = [] # works with candidate_counts indexed in same order
    voters =[]
    votes = []
    candidateresults = []
    candidate_counts = [] #list in order of candidates indexed the same as list "candidates"

    for row in csvelections:
        voters.append(str(row[0]))
        votes.append(str(row[2]))
        if candidates.count(str(row[2])) == 0:
            candidates.append(str(row[2]))
#This creates a list of the vote counts by candidate indexed in the same order as the list of candidates
    for candidate in candidates:
        a=votes.count(candidate)
        candidate_counts.append(a)

    totalvotes = str(len(voters))
    totalcandidates = str(len(candidates))
    
    #Generates a list called Results used in the variable 'printandcsv'
    Results = []
    Results_percent = [] #list of results used to determine the winner
    for b in range(int(totalcandidates)):
        c = str(f"{candidates[b]}:{format((candidate_counts[b]/sum(candidate_counts)),'.0%')} ({candidate_counts[b]}) ")
        Results.append(c)
        Results_percent.append(format((candidate_counts[b]/sum(candidate_counts)),'.0%'))

    #Winner determination
    winner = candidates[(Results_percent.index(max(Results_percent)))]
    
   
    printandcsv = str(f"Election Results\n ----------\n{Results[0]}\n{Results[1]}\n{Results[2]}\n{Results[3]}\n----------\nWinner: {winner} \n----------")

    print(printandcsv)

    textfile = open("Electionresults.txt", "w")
    textfile.write(printandcsv)                                                             