# Modules to create a file path across the operating system and read the csv, respectively
import os
import csv

# Set a path for the csv file
budget_csv = os.path.join("..", "PyBank", "budget_data.csv")

# Created lists to store the data
months = []
PnL = []
monthly_change = []

# Open and read the csv file
with open(budget_csv, newline="", encoding="utf-8") as budget_csv:
    csvreader = csv.reader(budget_csv, delimiter=",")
    
    # Read the header row
    header = next(csvreader)
    
    # Loop through the rows of the entire csv
    for row in csvreader:
        # Calculate the total number of months
        months.append(row[0])
        total_months = len(list(months))
        
        # Calculate the net total PnL over the entire period
        PnL.append(int(row[1]))
        net_PnL = sum(PnL)
    
    # Loop through the rows to find the monthly change in PnL (row[1]) date
    for i in range(len(PnL) - 1):
        # Calculate the monthly PnL changes
        monthly_change.append(PnL[i + 1] - PnL[i])

# The greatest increase and decrease in profits and the month in which each occurred
greatest_increase = max(monthly_change)
greatest_increase_month = months[monthly_change.index(greatest_increase) + 1]
greatest_decrease = min(monthly_change)
greatest_decrease_month = months[monthly_change.index(greatest_decrease) + 1]

# Find the average PnL change over the entire period
average_change = round((sum(monthly_change)/(len(monthly_change))), 2)

# Organize the output
print("Financial Analysis")
print("---------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_PnL}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})")

# Create a variable for the output file
output_file = ("../PyBank/Financial_Analysis.txt")

# Open and write in the output txt file
with open(output_file, "w", newline="") as f:
    print("Financial Analysis", file=f)
    print("---------------------------", file=f)
    print(f"Total Months: {total_months}", file=f)
    print(f"Total: ${net_PnL}", file=f)
    print(f"Average Change: ${average_change}", file=f)
    print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})", file=f)
    print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})", file=f)
    f.close()
