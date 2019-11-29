## Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.abspath("Resources/election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join(os.path.dirname(os.path.abspath(__file__)) + "/analysis/election_results.txt")


print(file_to_save)

# Initialize a total vote counter.
total_votes = 0

# Candidate Options
candidate_options = []
# 1. Declare the empty dictionary.
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

counties = []
county_dict = {}
county_name = ""

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1
        # Print the candidate name from each row.
        candidate_name = row[2]

# If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0

        candidate_votes[candidate_name] += 1

        # Print the candidate name from each row.
        county_name = row[1]

# If the candidate does not match any existing candidate...
        if county_name not in counties:
            # Add it to the list of candidates.
            counties.append(county_name)
            county_dict[county_name] = 0

        county_dict[county_name] += 1

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:

        # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results Per County\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n")
    print(election_results, end="")


    # Save the final vote count to the text file.
    txt_file.write(election_results)

    txt_file.write("County Votes:\n")

    # Determine the percentage of votes for each candidate by looping through the counts.
    # 1. Iterate through the candidate list.
    for county in counties:

        # 2. Retrieve vote count of a candidate.
        votes = county_dict[county]

        # 3. Calculate the percentage of votes.
        vote_percentage = int(votes) / int(total_votes) * 100

        # 4. Print the candidate name and percentage of votes.
        print(f"{county:4}: received {vote_percentage:2.1f}% of the vote.") 
  
        # Determine winning vote count and candidate
        # 1. Determine if the votes are greater than the winning count.
        #print(f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
        county_results = (f"{county}: {vote_percentage:.2f}% ({votes:,})\n")
        txt_file.write(county_results)
        if (votes > winning_count) and (vote_percentage > winning_percentage):
                # 2. If true then set winning_count = votes and winning_percent =
                # vote_percentage.
                winning_count = votes
                winning_percentage = vote_percentage
                # 3. Set the winning_candidate equal to the candidate's name.
                winning_county = county
    
    largest_county_summary = (
    f"\n-------------------------\n"
    f"Largest County Turnonver: {winning_county}\n"
    f"-------------------------\n\n")
    print(largest_county_summary)                
    txt_file.write(largest_county_summary) 

    
    for candidate in candidate_votes:
        # 2. Retrieve vote count of a candidate.
        votes = candidate_votes[candidate]
        # 3. Calculate the percentage of votes.
        vote_percentage = int(votes) / int(total_votes) * 100
        # 4. Print the candidate name and percentage of votes.
        print(f"{candidate}: received {vote_percentage:.1f}% of the vote.") 
        # Determine winning vote count and candidate
        # 1. Determine if the votes are greater than the winning count.
        #print(f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
        candidate_results = (f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        txt_file.write(candidate_results)
        if (votes > winning_count) and (vote_percentage > winning_percentage):
                # 2. If true then set winning_count = votes and winning_percent =
                # vote_percentage.
                winning_count = votes
                winning_percentage = vote_percentage
                # 3. Set the winning_candidate equal to the candidate's name.
                winning_candidate = candidate
    
    winning_candidate_summary = (
    f"\n-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
    print(winning_candidate_summary)                
    txt_file.write(winning_candidate_summary)  



   