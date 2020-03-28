# Import dependencies
import csv

# Declare variables
results = {}

# Read in CSV

# Calculate total number of votes

# List of candidates who received votes

# Percentage of votes won by each candidate

# Total of votes won by each candidate

# Winner of election based on popular vote

# Print output to terminal and to .txt file
output = (
    f'\nElection Results\n'
    f'---------------------\n'
    f'Total Votes: \n'
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