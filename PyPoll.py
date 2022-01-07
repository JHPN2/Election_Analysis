# The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

import csv
import os

# Diret Path to File
# assign a variable for the file to load and the path.
# file_to_load = 'Resources/election_results.csv'

# # Open the election results and read the file.
# # [DELETE, old way] election_data = open(file_to_load, 'r')
# with open(file_to_load) as election_data: # ends with a ':' so need to indent next line...

#     # to do: perform analysis.
#     print(election_data)

#close the file.
# [DELETE, old way] election_data.close()

# Indirect Path to File
file_to_load = os.path.join("Resources","election_results.csv")
# Open the election results and read the file.
with open(file_to_load) as election_data: # ends with a ':' so need to indent next line...

    # to do: perform analysis.
    print(election_data)

# Writing to Files
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the open() function with the "w" mode we will write data to the file.
open(file_to_save, "w")

# [DELETE] Test Writing to Files
# # Create a filename variable to a direct or indirect path to the file.
# file_to_save = os.path.join("analysis", "election_analysis.txt")

# # Use the open statement to open the file as a text file.
# outfile = open(file_to_save, "w")
# # Write some data to the file.
# outfile.write("Hello World")

# # Close the file
# outfile.close()

# Test Writing to Files using 'with'
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

    # Write some data to the file.
    # txt_file.write("Hello World")
    # txt_file.write("Arapahoe, ")
    # txt_file.write("Denver, ")
    # txt_file.write("Jefferson")
    # adding \n to force next line:
    txt_file.write("Counties in the Election\n------------------------\nArapahoe\nDenver\nJefferson")

#######################################################################

# 3.4.4
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here.
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Print each row in the CSV file
    # for row in file_reader:
    #     print(row)
    headers = next(file_reader)
    print(headers)