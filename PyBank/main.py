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

##average of changes##
list_changes = []    #create empty list
i = 1                 #set start index
stop = len(budget_df)  #set stop index

#loop through data
while i < stop:
    change = budget_df["Profit/Losses"][i] - budget_df["Profit/Losses"][i-1]    #calculate change
    list_changes.append(change)    #add value of change to list
    i += 1    #next row

avg_change = sum(list_changes) / len(list_changes)    #calculate average
avg_change = round(avg_change, 2)    #format to 2 decimal places