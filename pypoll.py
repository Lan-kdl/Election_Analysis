import csv
import os 
# Assign a variable for the file to load and the path 
file_to_load = os.path.join("Resources","election_results.csv")

# Open the election results and read the file
with open(file_to_load) as election_data:
    #To Do: Read the data here
    file_reader = csv.reader(election_data)

    # Read and print the header row
    headers = next(file_reader)
    print(headers)
# Create a file name variable to a direct or indirect path to a file
file_to_save = os.path.join("analysis","election_analysis.txt")
# Using the open function with the "w" mode we will write data to the file 
with open(file_to_save,"w") as txt_file:
    txt_file.write("Counties in the Election\n---------------------\nArapahoe,\nDenver,\nJefferson")