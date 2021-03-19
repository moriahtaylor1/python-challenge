##load dependencies##
import pandas as pd
import sys
import os

#read in csv file
election_df = pd.read_csv("Resources/election_data.csv")
#convert to pandas dataframe
election_df = pd.DataFrame(election_df)
