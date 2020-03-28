# Import dependencies
import csv

# Declare variables
votes = []
results = {}

# Read in CSV
import_path = "election_data.csv"
with open(import_path, newline='') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ',')
    header = next(csv_reader)

    for row in csv_reader:
        votes.append(row[2])

# Calculate total number of votes
total_votes = len(votes)

# List of candidates who received votes
candidates = list(set(votes))

# Total votes won by each candidate
for candidate in candidates:
    results.setdefault(candidate, votes.count(candidate))

# Winner of election based on popular vote
winner = max(set(votes), key=votes.count)

# Print output to terminal and to .txt file
output = (
    f'\nElection Results\n'
    f'---------------------\n'
    f'Total Votes: {total_votes}\n'
    f'---------------------\n'
    f'Name: % (total)\n'
    f'---------------------\n'
    f'Winner: {winner}\n'
    f'---------------------\n'
)

print(output)

export_path = "results.txt"
with open(export_path, 'w') as txt_file:
    txt_file.write(output)