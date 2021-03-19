##load dependencies##
import pandas as pd
import sys
import os

#read in csv file
election_df = pd.read_csv("Resources/election_data.csv")
#convert to pandas dataframe
election_df = pd.DataFrame(election_df)

##total number of votes##
total_votes = len(election_df)

##list of candidates##
candidates = election_df["Candidate"].unique()