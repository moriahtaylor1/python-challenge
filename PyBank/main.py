##load dependencies##
import pandas as pd
import sys
import os

#read in csv file
budget_df = pd.read_csv("Resources/budget_data.csv")
#convert to pandas dataframe
budget_df = pd.DataFrame(budget_df)

##total nums of months##
num_months = len(budget_df)

##net amount of profit/losses##
net_total = budget_df["Profit/Losses"].sum()
