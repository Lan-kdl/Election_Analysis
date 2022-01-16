import csv
import os 
# Assign a variable for the file to load and the path 
file_to_load = os.path.join("Resources","election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
#Initialize a total vote counter
total_votes = 0 
# Declare a new list
candidate_options = []
# Declare an empty dictionary
candidate_votes = {}
# Declare a winning candidate
winning_candidate = ""
# Declare an integer winning count
winning_count = 0
# Declare a winning percentage
winning_percentage = 0

# Open the election results and read the file
with open(file_to_load) as election_data:
    #To Do: Read the data here
    file_reader = csv.reader(election_data)

    # Read and print the header row
    headers = next(file_reader)
    
    # Print each row in the csv file
    for row in file_reader:
        # Add to the total vote count
        total_votes += 1

        # Print the candidate name for each row
        candidate_name = row[2]

        # If the candidate does not match any exsisting candidate 
        if candidate_name not in candidate_options:
            # Add it to the list of candidates
            candidate_options.append(candidate_name)

            # Begin tracking that candidate's vote count
            candidate_votes[candidate_name] = 0

        # Increment the votes
        candidate_votes[candidate_name] += 1

#save the results to our text file
with open(file_to_save, "w") as txt_file:
    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)

#Use a for loop to iterate through the candidate_options = [] list
    for candidate_name in candidate_votes:
        #Use the for loop variable to retrieve the votes of the candidate from the candidate_votes = {} dictionary.
        votes = candidate_votes[candidate_name]
        #Calculate the percentage of the vote count.
        vote_percentage = float(votes) / float(total_votes) * 100

        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate, their vote count, and percentage to the terminal 
        print(candidate_results)

        # Save the candidate results to our text file 
        txt_file.write(candidate_results)

        # Determine winning vote count candidate
        # Determine if the votes are greater than the winning count
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true then set winning count = votes and winning_percent = vote_percent
            winning_count = votes
            winning_percentage = vote_percentage
            # Set the winning_candidate = to the candidate's name
            winning_candidate = candidate_name

    winning_candidate_summary = (
        f'-------------------------\n'
        f'Winner: {winning_candidate}\n'
        f'Winning Vote Count: {winning_count:,}\n'
        f'Winning Percentage: {winning_percentage:.1f}%\n'
        f'-------------------------\n')
    # Print the winning candidate, vote count, and percentage to terminal 
    #print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
    print(winning_candidate_summary)

# Save the winning candidates name to the text file
    txt_file.write(winning_candidate_summary)