import os
import csv
import pandas as pd 

budget_data =  os.path.join("C:\\Users\\maris\\Data Analyst\\python-challenge\\PyBank\\Resources\\budget_data.csv")
# budget_data =  os.path.join("Pybank","Resources","budget_data.csv")
with open(budget_data, "r") as csv_file:
    budget_data = csv.reader(csv_file)
    next(budget_data)
    # next(budget_data)
    total_months=0
    for row in budget_data:
        # print(row)
        total_months=total_months+1
        # total_months+=1
print(f'Financial Analysis')
print(f'-------------------------')
print(f'Total Months: {total_months}')

budget_data =  os.path.join("C:\\Users\\maris\\Data Analyst\\python-challenge\\PyBank\\Resources\\budget_data.csv")
with open(budget_data, "r") as csv_file:
    df = pd.read_csv(budget_data)
    # Calculate the total of a specific column, for example 'Profit/Losses'
    # net_total = df['Profit/Losses'].sum()
    for row in 'Profit/Losses':
        net_total = df['Profit/Losses'].sum()

print(f'Total: ${net_total}')


#      df['Profit/Losses'] = df['Profit/Losses'].diff
#      Average_Change = df ["Profit/Losses"].mean()
# print(f'Total Average: {Average_Change}')

# Assuming budget_data.csv is located in the Resources folder relative to the current script
budget_data = os.path.join("C:\\Users\\maris\\Data Analyst\\python-challenge\\PyBank\\Resources\\budget_data.csv")
with open(budget_data, "r") as csv_file:
    df = pd.read_csv(budget_data)
# Calculate the differences (changes) in Profit/Losses column
    df['Change'] = df['Profit/Losses'].diff()
# Calculate the average change
    average_change = df['Change'].mean()
    rounded_average_change = round(average_change, 2)

print(f"Average Change: {rounded_average_change}")

budget_data = os.path.join("C:\\Users\\maris\\Data Analyst\\python-challenge\\PyBank\\Resources\\budget_data.csv")
with open(budget_data, "r") as csv_file:
    df = pd.read_csv(budget_data)
    df['Change'] = df['Profit/Losses'].diff()
    greatest_increase = df.loc[df["Change"].idxmax()]
    date_greatest_profit= greatest_increase['Date']
    greatest_increase_amount= greatest_increase['Change']
    greatest_increase_int = int(greatest_increase_amount)
print(F'Greatest Increase in Profits: {date_greatest_profit} ${greatest_increase_int}')

budget_data = os.path.join("C:\\Users\\maris\\Data Analyst\\python-challenge\\PyBank\\Resources\\budget_data.csv")
with open(budget_data, "r") as csv_file:
    df = pd.read_csv(budget_data)
    df['Change'] = df['Profit/Losses'].diff()
    greatest_decrease = df.loc[df["Change"].idxmin()]
    date_decreased_profit= greatest_decrease['Date']
    greatest_decrease_amount= greatest_decrease['Change']
    greatest_decrease_int = int(greatest_decrease_amount)
print(F'Greatest Decrease in Profits: {date_decreased_profit} ${greatest_decrease_int}')
  
#NOW I HAVE TO EXPORT A TEXT FILE WITH MY RESULTS#######
final_analysis = os.path.join("C:\\Users\\maris\\Data Analyst\\python-challenge\\PyBank\\Analysis\\Final Results")

with open(final_analysis, "w") as file:
    file.write("Financial Analysis\n")
    file.write("-------------------------\n")
    file.write(f"Total Months: {total_months}\n")
    file.write(f"Total: ${net_total}\n")
    file.write(f"Average Change: ${rounded_average_change}\n")
    file.write(f"Greatest Increase in Profits: {date_greatest_profit} (${int(greatest_increase_amount)})\n")
    file.write(f"Greatest Decrease in Profits: {date_decreased_profit} (${int(greatest_decrease_amount)})\n")

print(f"Results have been written to {final_analysis}")