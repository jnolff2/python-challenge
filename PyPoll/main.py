# Modules to create a file path across the operating system and read the csv, respectively
import os
import csv

# Set a path for the csv
election_csv = os.path.join("..", "PyPoll", "election_data.csv")

# Create list of variables
total_votes = 0
votes_Khan = 0
votes_Correy =0
votes_Li = 0
votes_OTooley = 0
election_winner = []

# Open and read the csv file
with open(election_csv, newline="", encoding="utf-8") as election_csv:
    csvreader = csv.reader(election_csv, delimiter=",")

    # Read the header row
    csvheader = next(csvreader)
   
   # Loop through the rows of the csv
    for row in csvreader:
        # Calculate the total number of votes cast
        total_votes = total_votes + 1
        
        # Use conditionals to count the number of votes each candidate received
        if row[2] == "Khan":
            votes_Khan = votes_Khan + 1
        elif row[2] == "Correy":
            votes_Correy = votes_Correy + 1
        elif row[2] == "Li":
            votes_Li = votes_Li + 1
        elif row[2] == "O'Tooley":
            votes_OTooley = votes_OTooley + 1

        # Use conditionals to determine which candidate received the most votes to win the election
        if votes_Correy > votes_Khan & votes_Correy > votes_Li & votes_Correy > votes_OTooley:
            election_winner = "Correy"
        elif votes_OTooley > votes_Correy & votes_OTooley > votes_Li & votes_OTooley > votes_Khan:
            election_winner = "OTooley"
        elif votes_Khan > votes_Correy & votes_Khan > votes_Li & votes_Khan > votes_OTooley:
            election_winner = "Khan"
        elif votes_Li > votes_Correy & votes_Li > votes_Khan & votes_Li > votes_OTooley:
            election_winner = "Li"


        # Calculate the percentage of the total vote that each candidate received
        vote_percentage_Khan = (votes_Khan / total_votes) * 100
        vote_percentage_Correy = (votes_Correy / total_votes) * 100
        vote_percentage_Li = (votes_Li / total_votes) * 100
        vote_percentage_OTooley = (votes_OTooley / total_votes) * 100


# Print the output
print("Election Results")
print("-----------------------")
print(f"Total Votes: {total_votes}")
print("-----------------------")
print(f"Khan: {str(round(vote_percentage_Khan, 3)) + '00%'} ({votes_Khan})")
print(f"Correy: {str(round(vote_percentage_Correy, 3)) + '00%'} ({votes_Correy})")
print(f"Li: {str(round(vote_percentage_Li, 3)) + '00%'} ({votes_Li})")
print(f"O'Tooley: {str(round(vote_percentage_OTooley, 3)) + '00%'} ({votes_OTooley})")
print("-----------------------")
print(f"Winner: {election_winner}")
print("-----------------------")

# Export the printed output to a .txt file
output_file = ("../PyPoll/Election_Results.txt")

# Open and write in the output file
with open(output_file, "w", newline="") as f:
    print("Election Results", file=f)
    print("-----------------------", file=f)
    print(f"Total Votes: {total_votes}", file=f)
    print("-----------------------", file=f)
    print(f"Khan: {str(round(vote_percentage_Khan, 3)) + '00%'} ({votes_Khan})", file=f)
    print(f"Correy: {str(round(vote_percentage_Correy, 3)) + '00%'} ({votes_Correy})", file=f)
    print(f"Li: {str(round(vote_percentage_Li, 3)) + '00%'} ({votes_Li})", file=f)
    print(f"O'Tooley: {str(round(vote_percentage_OTooley, 3)) + '00%'} ({votes_OTooley})", file=f)
    print("-----------------------", file=f)
    print(f"Winner: {election_winner}", file=f)
    print("-----------------------", file=f)
    f.close()
