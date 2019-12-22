import os
import csv

     
#Path to collect data from the Resources folder

PyPoll_csv = os.path.join( 'Resources', 'election_data.csv')

#The total number of votes cast

#A complete list of candidates who received votes

#The percentage of votes each candidate won

#The total number of votes each candidate won

#The winner of the election based on popular vote.

#Election Results
#-------------------------
#Total Votes: 3521001
#-------------------------
#Khan: 63.000% (2218231)
#Correy: 20.000% (704200)
#Li: 14.000% (492940)
#O'Tooley: 3.000% (105630)
#-------------------------
#Winner: Khan
#-------------------------

 #Open and read csv
with open(PyPoll_csv, 'r') as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=",")
  # Read the header row first (skip this part if there is no header) 
    
    header = next(csvreader)
    Total_votes= 1
    votes_Khan= 0
    votes_Li = 0
    votes_Correy = 0
    votes_other =0 

    #print(header)
    #print (previous)

    # looping thorugh the file 
        
    for row in csvreader:
       #print(row)
        current = (row[2])
        #print (current)
        Total_votes = Total_votes + 1
        if current == "Khan":
            votes_Khan = votes_Khan+1
        if current == "Li":
            votes_Li = votes_Li +1  
        if current == "Correy":
            votes_Correy=votes_Correy +1 
        if current!= "Khan" and current!="Li" and current!= "Correy":
            votes_other=votes_other+1
        
        
Percentage_Khan = (votes_Khan/Total_votes)*100
Percentage_Correy = (votes_Correy/Total_votes)*100
Percentage_Li = (votes_Li/Total_votes)*100
Percentage_other = (votes_other/Total_votes)*100
if Percentage_Correy> Percentage_Khan and Percentage_Correy> Percentage_Li and Percentage_Correy> Percentage_other:
    Winner= "Correy"
if Percentage_Khan> Percentage_Correy and Percentage_Khan> Percentage_Li and Percentage_Khan> Percentage_other:
    Winner = "Khan"
if Percentage_Li>Percentage_Correy and Percentage_Li> Percentage_Khan and Percentage_Li> Percentage_other:
    Winner = "Li"
if  Percentage_other>Percentage_Correy and Percentage_other> Percentage_Khan and Percentage_other> Percentage_Li:
    Winner = "other"

print("Election Results")
print("-----------------------")
print(f'Total Votes: { Total_votes}')
print("-------------------------")
print(f'Khan: {Percentage_Khan:.3f}% {votes_Khan}')
print(f'Correy {Percentage_Correy:.3f}% {votes_Correy}')
print(f'Li {Percentage_Li:.3f}% {votes_Li}')
print(f"O'tooley {Percentage_other:.3f}%  {votes_other}")
print("-------------------------")
print(f'Winner: {Winner}')
print("-------------------------")

PyPoll_outcsv = os.path.join( 'Resources', 'PyPoll_data.csv')
with open(PyPoll_outcsv, 'w', newline='') as csvfile1:
    csvwriter = csv.writer(csvfile1, delimiter=',')
    csvwriter.writerow (["Election Results"])
    csvwriter.writerow (["-----------------------"])
    csvwriter.writerow ([f'Total Votes: { Total_votes}'])
    csvwriter.writerow (["-------------------------"])
    csvwriter.writerow ([f'Khan: {Percentage_Khan:.3f}% {votes_Khan}'])
    csvwriter.writerow ([f'Correy {Percentage_Correy:.3f}% {votes_Correy}']) 
    csvwriter.writerow ([f'Li {Percentage_Li:.3f}% {votes_Li}'])
    csvwriter.writerow ([f"O'tooley {Percentage_other:.3f}%  {votes_other}"])
    csvwriter.writerow (["-------------------------"])
    csvwriter.writerow ([f'Winner: {Winner}'])
    csvwriter.writerow (["-------------------------"])
