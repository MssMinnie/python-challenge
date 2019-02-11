import os
import csv

csvpath = './budget_data.csv'
    
budget = []
changes = []
best_increase = ["", 0]
worst_decrease = ["", 0]
num_months = 0
total = 0
monthly_change = 0
previous = 0

# Read in the CSV file
with open(csvpath, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
	
	# Read the header row
    csv_header = next(csvreader)
    budget.append(csv_header)

    # Read each row of data after the header
    for row in csvreader:
        
        num_months += 1        # add to month count
        amount = int(row[1])   # get amount for the month
        total += amount        # add to the running total
      
        monthly_change = int(row[1]) - previous
        previous = int(row[1])
        
        if (monthly_change > best_increase[1]):
            best_increase[1] = monthly_change
            best_increase[0] = row[0]
            
        if (monthly_change < worst_decrease[1]):
            worst_decrease[1] = monthly_change
            worst_decrease[0] = row[0]
            
        changes.append(int(row[1]))
        average = sum(changes) / len(changes)

    print('Financial Analysis\n' '--------------------')        
    print(f"Total months : {num_months}")
    print(f"Total: ${total}")
    print(f"Average change : ${average}")
    print(f"Greatest Increase in Profits: {(best_increase[0])} (${best_increase[1]})")
    print(f"Greatest Decrease in Profits: {(worst_decrease[0])} (${worst_decrease[1]})")
    
output_file = os.path.join("..", "output", budget.txt")