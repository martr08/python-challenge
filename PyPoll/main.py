import os
import csv
import pandas as pd 

election_df = os.path.join("C:\\Users\\maris\\Data Analyst\\python-challenge\\PyPoll\\Resources\\election_data.csv")

with open(election_df,"r") as csv_file:
    election_df = csv.reader(csv_file)
    next(election_df)
    total_votes=0
    for row in election_df:
        total_votes=total_votes+1
print(f'Election Results')
print(f'------------------------')
print(f'Total Votes:{total_votes}')
print(f'------------------------')

election_df = pd.read_csv("C:\\Users\\maris\\Data Analyst\\python-challenge\\PyPoll\\Resources\\election_data.csv")

ccs_vote='Charles Casper Stockham'
vote_charles=(election_df['Candidate']==ccs_vote).sum()
percentage_charles= ((vote_charles/total_votes)*100)
print(f'Charles Casper Stockham: {round(percentage_charles,3)}% ({vote_charles})')

dd_vote = 'Diana DeGette'
vote_diana=(election_df['Candidate']==dd_vote).sum()
percentage_diana=(vote_diana/total_votes)*100
print(f'Diana DeGette: {round(percentage_diana,3)}% ({vote_diana})')

rad_vote = 'Raymon Anthony Doane'
vote_raymon=(election_df['Candidate']==rad_vote).sum()
percentage_raymon=(vote_raymon/total_votes)*100
print(f'Raymon Anthony Doane: {round(percentage_raymon,3)}% ({vote_raymon})')
print(f'------------------------')

election_df = pd.read_csv("C:\\Users\\maris\\Data Analyst\\python-challenge\\PyPoll\\Resources\\election_data.csv")
vote_counts = election_df['Candidate'].value_counts()

elected_winner = vote_counts.idxmax()


print(f'Winner: {elected_winner}')
print(f'------------------------')

final_analysis = os.path.join('C:\\Users\\maris\\Data Analyst\\python-challenge\\PyPoll\\Analysis\\Final Results')

with open(final_analysis,"w") as file:
    file.write("Election Results\n")
    file.write("------------------------\n")
    file.write(f"Total Votes:{total_votes}\n")
    file.write("------------------------\n")
    file.write(f"Charles Casper Stockham: {round(percentage_charles,3)}% ({vote_charles})\n")
    file.write(f"Diana DeGette: {round(percentage_diana,3)}% ({vote_diana})\n")
    file.write(f"Raymon Anthony Doane: {round(percentage_raymon,3)}% ({vote_raymon})\n")
    file.write("------------------------\n")
    file.write(f"Winner: {elected_winner}\n")
    file.write("------------------------\n")

print(f"Results have been written to {final_analysis}")