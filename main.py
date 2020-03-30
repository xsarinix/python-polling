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

# Summarize results and export to file
output_path = "results.txt"
with open(output_path, "w") as txt_file:

    # Calculate total number of votes, print to terminal, and write to file
    total_votes = len(votes)
    totals_output = (
        f'\nElection Results\n'
        f'---------------------\n'
        f'Total Votes: {total_votes:,.0f}\n'
        f'---------------------\n'
    )
    print(totals_output, end="")
    txt_file.write(totals_output)


    # List of candidates who received votes
    candidates = list(set(votes))

    # Total votes won by each candidate, print to terminal, and write to file
    for candidate in candidates:
        results.setdefault(candidate, votes.count(candidate))
        vote_percent = results[candidate] / total_votes * 100
        candidate_output = f'{candidate}: {vote_percent:.1f}% ({results[candidate]:,.0f})\n'
        print(candidate_output, end="")
        txt_file.write(candidate_output)

    # Winner of election based on popular vote, print to terminal, and write to file
    winner = max(set(votes), key=votes.count)
    winner_output = (
        f'---------------------\n'
        f'Winner: {winner}\n'
        f'---------------------\n'
    )
    print(winner_output, end="")
    txt_file.write(winner_output)