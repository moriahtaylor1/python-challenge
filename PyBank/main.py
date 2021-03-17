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

##greatest increase in profits##
max_inc = max(budget_df["Profit/Losses"])    #find greatest increase
max_inc_row = budget_df[budget_df["Profit/Losses"]==max_inc]   #get row
max_inc_date = max_inc_row.iloc[0,0]    #pull date from row

##greatest decrease in profits##
max_dec = min(budget_df["Profit/Losses"])    #find greatest decrease
max_dec_row = budget_df[budget_df["Profit/Losses"]==max_dec]    #get row
max_dec_date = max_dec_row.iloc[0,0]    #pull date from row

##output analysis table as .txt file##

#change directory to Analysis folder
os.chdir('../PyBank/Analysis')

#create .txt file
with open('analysis.txt', 'w') as f:
    #write in file
    print('Financial Analysis', end='\n', file=f)
    print('----------------------------', end='\n', file=f)
    print(f'Total Months: {num_months}', end='\n', file=f)
    print(f'Total: ${net_total}', end='\n', file=f)
    print(f'Average Change: ${avg_change}', end='\n', file=f)
    print(f'Greatest Increase in Profits: {max_inc_date} (${max_inc})', end='\n', file=f)
    print(f'Greatest Decrease in Profits: {max_dec_date} (${max_dec})', file=f)

#read .txt file so it prints out in console
with open('analysis.txt', 'r') as f:
    text = f.read()
    print(text)
    f.close()
