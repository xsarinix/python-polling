# Import dependencies
import csv

# Declare variables
votes = {}
voter_ids = []
results = {}

# Read in CSV
import_path = "election_data.csv"
with open(import_path, newline='') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ',')
    header = next(csv_reader)

    for row in csv_reader:
        voter_ids.append(row[0])
        votes.setdefault(row[2], []).append(row[0])

# Calculate total number of votes
total_votes = len(set(voter_ids))

# List of candidates who received votes
candidates = list(results.keys())

# Total votes and percentage of votes won by each candidate
for candidate in votes:
    results.setdefault(candidate, {})
    results[candidate].setdefault("Total Votes", len(votes[candidate]))
    results[candidate].setdefault("Percentage of Votes", len(votes[candidate])/total_votes)

print(results)

# Winner of election based on popular vote

# Print output to terminal and to .txt file
output = (
    f'\nElection Results\n'
    f'---------------------\n'
    f'Total Votes: {total_votes}\n'
    f'---------------------\n'
    f'Name: % (total)\n'
    f'---------------------\n'
    f'Winner: \n'
    f'---------------------\n'
)

print(output)

export_path = "results.txt"
with open(export_path, 'w') as txt_file:
    txt_file.write(output)