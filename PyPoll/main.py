import os
import csv
csvpath = os.path.join( 'Resources', "election_data.csv")

votes = 0
voteCount = {}



with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile)
    csv_header = next(csvreader)

    for row in csvreader:

        votes += 1

        candidate = row[2]

        if candidate in voteCount:
            voteCount[candidate] += 1

        else:
            voteCount[candidate] = 1
                
    
            
totalVotes = sum(voteCount.values())
winner = max(voteCount, key=voteCount.get)

outputText = (

"Election Results\n"
" \n"
"---------------------------\n"
" \n"
f"Total Votes: {votes} \n"
" \n"
"---------------------------\n"
" \n"
)
for candidate, count in voteCount.items():
    percentage = round((count / totalVotes) * 100, 3)
    outputText += f"{candidate}: {percentage}% ({count})\n"
    
outputText += (  
" \n"
"---------------------------\n"
" \n"
f"Winner: {winner} \n"
" \n"
"---------------------------\n"
)

print(outputText)
outputPath = os.path.join('Analysis', 'new.txt')

with open(outputPath, 'w') as txtfile:
    txtfile.write(outputText)