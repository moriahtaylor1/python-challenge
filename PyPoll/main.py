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
khan_perc = round(vote_perc[0], 2)    #save each candidate's percentage as rounded integer
correy_perc = round(vote_perc[1], 2)
li_perc = round(vote_perc[2], 2)
otooley_perc = round(vote_perc[3], 2)

##vote per candidate##
vote_count = Counter(election_df["Candidate"])

#put vote counts into dictionary
max_votes=max(vote_count.values())     #put max num of votes in a variable
winners =[i for i in vote_count.keys() if vote_count[i]==max_votes]    #find name of winner
winner = winners[0]    #abstract name of winner from list