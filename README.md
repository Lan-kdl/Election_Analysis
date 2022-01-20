# Election_Analysis

## Project Overview
A Colorado Board of Elections emplyee has tasked me with completing an election audit of a recent, local congressional election. 

1. Calculate the total number of votes cast. 
2. Get a complete list of candidates who have received votes. 
3. Calculate the total number of votes each candidate received. 
4. Caluculate the percentage of votes each candidate won. 
5. Determine the winner of the election based on popular vote. 

## Resources
- Data source: Election_Results.csv
- Software: Python 3.9.7, Visual Studio Code

## Summary 
The analysis of the election show that: 
- There were 369,711 votes cast in the election
- The candidates were: 
  1. Charles Casper Stockham
  2. Diana DeGette
  3. Raymon Anthony Doane
- The candidate results were: 
  - Charles Casper Stockham recieved 23% of the votes and 85, 213 number of votes.
  - Diana DeGette recieved 73.8% of the votes and 272,892 number of votes. 
  - Raymon Anthony Doane received 3.1% of the votes and 11,606 number of votes. 
- The winner of the election was: 
  Diana DeGette who received 73.8% of the votes and 272,892 number of votes. 
  
 ## Challenge Overview
 Using the ELection_Results.csv file for the source of the data, I began by printing importing csv and os packages. I then imported the csv file and created a text file to output the results. I set the total_votes variable to zero and then created a candidate_options list and a candidate_votes dictionary. I also created a winning_candidate variable and set the winning_count and winning_percentage variables to zero. I then read the election_results file and printed the headers as well as the rows. For each candidate, I added to the total votes and added the names of the candidates to the candidate_options list. I imported the total_votes to the text file. I then calculated the vote_percentage for each candidate in the loop, and wrote these results to my text file. I then determined the winner using an if statement, and printed these results to the terminal and text file. 
 
 ## Challenge Summary 
 To analyize the local election, I had to first import the Election_Results.csv file and print the data to the terminal. From there, I could print the total vote count, the names of the candidates, and the number of votes they recieved to the terminal. I then calculated the percentage of votes for each candidate and determined the winner. I imported these results to a text file.  
