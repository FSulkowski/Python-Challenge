import os

import csv

csvpath = os.path.join( 'Resources', 'budget_data.csv')


months = 0
total = 0
averageChange = []
profitChange = []
increase = None
decrease = None
previousValue = None



with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile)
    csv_header = next(csvreader)
    
    previousValue = None
    
    for row in csvreader:
      
        total += float(row[1])
        months += 1
        currentValue = float(row[1])


        if previousValue is not None:
            change = currentValue - previousValue
            averageChange.append(change)

    
        if previousValue is not None:
            change = currentValue - previousValue
            profitChange.append(change)
            
            if increase is None or change > increase[1]:
                increase = [row[0], change]
            if decrease is None or change < decrease[1]:
                decrease = [row[0], change]

        previousValue = currentValue

if len(averageChange) > 0:
    averageChangeValue = sum(averageChange) / len(averageChange)
else:
    averageChangeValue = 0

outputText = (

"Financial Analysis\n"

"---------------------------\n"

f"Total Months: {months}\n"

f"Total: ${round(total)}\n"

f"Average Change: ${averageChangeValue:.2f}\n"

f"Greatest Increase in Profits: {increase[0]} (${round(increase[1])})\n"

f"Greatest Decrease in Profits: {decrease[0]} (${round(decrease[1])})\n"
)
print(outputText)
outputPath = os.path.join('Analysis', 'new.txt')

with open(outputPath, 'w') as txtfile:
    txtfile.write(outputText)