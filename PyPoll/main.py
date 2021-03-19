##load dependencies##
import pandas as pd
import sys
import os
from collections import Counter

#read in csv file
election_df = pd.read_csv("Resources/election_data.csv")
#convert to pandas dataframe
election_df = pd.DataFrame(election_df)

##total number of votes##
total_votes = len(election_df)

##list of candidates##
candidates = election_df["Candidate"].unique()

##percentage of votes per candidate##
vote_perc = election_df["Candidate"].value_counts(normalize=True)    #get percentages
vote_perc = [v*100 for v in vote_perc]    #multiply by 100 for formatting
khan_perc = round(vote_perc[0], 1)    #save each candidate's percentage as rounded integer
correy_perc = round(vote_perc[1], 1)
li_perc = round(vote_perc[2], 1)
otooley_perc = round(vote_perc[3], 1)

##vote per candidate##
vote_count = Counter(election_df["Candidate"])
vote_count["OTooley"] = vote_count["O'Tooley"]    #change to avoid error later when writing txt file

##get winner##
#put vote counts into dictionary
max_votes=max(vote_count.values())     #put max num of votes in a variable
winners =[i for i in vote_count.keys() if vote_count[i]==max_votes]    #find name of winner
winner = winners[0]    #abstract name of winner from list

##output table as .txt file##

#change directory to Analysis folder
os.chdir('../PyPoll/Analysis')

#create .txt file
with open('analysis.txt', 'w') as f:
    #write in file
    print('Election Results', end='\n', file=f)
    print('-------------------------', end='\n', file=f)
    print(f'Total Votes: {total_votes}', end='\n', file=f)
    print('-------------------------', end='\n', file=f)
    print(f'Khan: {khan_perc}00% ({vote_count["Khan"]})', end='\n', file=f)
    print(f'Correy: {correy_perc}00% ({vote_count["Correy"]})', end='\n', file=f)
    print(f'Li: {li_perc}00% ({vote_count["Li"]})', end='\n', file=f)
    print(f'O\'Tooley: {otooley_perc}00% ({vote_count["OTooley"]})', end='\n', file=f)
    print('-------------------------', end='\n', file=f)
    print(f'Winner: {winner}', end='\n', file=f)
    print('-------------------------', end='\n', file=f)

#read .txt file so it prints out in console
with open('analysis.txt', 'r') as f:
    text = f.read()
    print(text)
    f.close()