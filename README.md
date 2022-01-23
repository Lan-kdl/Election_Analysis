# Election_Analysis

## Project Overview

The purpose of this election audit analysis was to fulfill the tasks assigned to me by a Colorado Board of Elections employee. I was to complete an election audit of a recent, local congressional election. The original data was a csv file which included the Ballot ID, County, and Candidate for each voter. My assignment was to analyze this data so that the outcome of the election audit was the winner of the election and the county with the most votes cast. 

[PyPoll_Challenge.py](https://github.com/Lan-kdl/Election_Analysis/blob/main/PyPoll_Challenge.py)

[Resources](https://github.com/Lan-kdl/Election_Analysis/tree/main/Resources) 

The [analysis folder](https://github.com/Lan-kdl/Election_Analysis/tree/main/analysis) containing the [election_results.txt](https://github.com/Lan-kdl/Election_Analysis/blob/main/analysis/election_analysis.txt)

## Election-Audit Results

* There were 369,711 votes cast in this local, congressional election. We found the total votes by first initializing a total_votes variable to zero. Then, we looped through each row in the original csv file, each time adding 1 vote to the total_vote variable. 

![Initialize_Vote_Counter](https://user-images.githubusercontent.com/95589611/150697502-e6df6eaa-5cd6-4e16-aa7e-f84b390a2352.png)

![loop_through_total_votes](https://user-images.githubusercontent.com/95589611/150697504-177e8ff5-086a-4709-bef9-887b763ff154.png)

![Total_Votes](https://user-images.githubusercontent.com/95589611/150697514-36b4f73b-3a83-4df6-bdef-6b5851f5305a.png)

* The number of votes and the percentage of total votes for each county in the precinct are as follows: 
  * Arapahoe had the least votes with 24,801 votes cast (6.7% of the total votes); 
  * Jefferson county had 38,855 votes and 10.5% of the total votes cast; 
  * Denver County had the most votes with 306,055 votes, leading to 82.8% of the total votes cast. 

The process of accuring these results began with creating an empty list that would hold the county_names and an empty dictionary that would hold the county name as a key and the number of votes for each county as the subsequent value. 

![create_county_list_and_county_votes](https://user-images.githubusercontent.com/95589611/150697584-70f70cb9-2c32-43d5-a150-e1ef1b80df47.png)

I then began extracting the county_name from each row within a for loop which iterated through all of the rows. 

![extracting_county_name](https://user-images.githubusercontent.com/95589611/150697611-0360624d-2759-4c85-a7dc-b21727ac2836.png)

Once I initialized the county_names, I created a conditional statement within the for loop which tested whether or not the current county_name was in the county_list. If the current county_name was not in the county_list, it was added to the list. I then initialized each county's vote count to zero and began to track the vote count for each county within the for loop where for each iteration one vote was added using the county_name as an index key. 

![county_conditional_statement](https://user-images.githubusercontent.com/95589611/150697651-073a05f9-70b2-4e52-ab46-15b740b1cb6d.png)

Now that I had the votes cast in each county along with the number of total votes, I determined the percentage of total votes cast for each county using a simple mathematical equation. Before I could exectute the equation, it was a good idea to create a seperate for loop to get the county_name from the county_votes dictionary so that I could get the vote_count for each county_name. I also had to convert vote_count and total_vote integers into a floating-point number using the float() function before I could execute my percentage equation. 

![county_vote_percentage](https://user-images.githubusercontent.com/95589611/150697722-0c83e023-2246-4e58-9563-c9cd1f8f29cd.png)

Finally, I had my percentage and vote count for each county. 

![County_Breakdown](https://user-images.githubusercontent.com/95589611/150697661-06d43cab-dee3-44a9-8bae-1f810bd52007.png)

* The county with the largest number of votes was Denver with 306,055 votes and 82.8% of the total votes. 

![largest_county](https://user-images.githubusercontent.com/95589611/150697762-6cfef1fd-e094-4ebd-ab2b-d4b927d27089.png)

* The number of votes and the percentage of the total votes for each candidate is as follows: 
  * Raymon Anthony Doane had the least amount of votes (11,606) with only 3,1% of the total votes cast; 
  * Charles Casper Stockham had 85,213 votes and 23% of the total votes, 
  * Diana DeGette had the most votes with 73.8% (272,892) of the total votes cast. 

The process for aquiring the vote count and percentage of total votes for each candidate was virtually the same as aquiring the vote count and percentage of votes for each county. The process began by initializing a list that would hold the candidate names and a dictionary that would use the names as a key and the votes as the values.

![candidate_list_and_dictionary](https://user-images.githubusercontent.com/95589611/150697800-3043443a-3c80-41a4-a5c3-de2b6862c1fd.png)

Within a for loop which iterated through the rows of the original csv file, I assigned candidate_name to the second index (row three) and wrote a conditional statement that tested whether or not the current candidate_name was in the candidate_options list and if it was not to add it using the append() funtion. Withing this for loop I also began tracking the candidate vote count by setting it to zero and then adding one vote everytime it iterated through the list making sure to use the candidate_name as the index. 

![candidate_vote_loop](https://user-images.githubusercontent.com/95589611/150698855-425c3df8-5ff0-4a68-bf5c-a8c4e02934b3.png)

To get the percentage of the candidate votes, I created a seperate for loop that would iterate through each of the candidate_names in the candidate_votes dictionary. Just like with the county_votes, I used the float() funtion to convert the integers into floating-point number so that I can execute the mathematical equation to aquire the percentage. 

![Candidate_percentage](https://user-images.githubusercontent.com/95589611/150697874-ce1262b0-67de-46b6-9f55-1a96be4a5deb.png)

Finally, I had the vote count along with the percentage of total votes for each candidate. 

![candidate_breakdown](https://user-images.githubusercontent.com/95589611/150697883-fe74d3e0-ff5e-4380-8e5b-a0cb20b1409d.png)

* Diana DeGette won the election with 272,892 votes and 73.8% of the total votes cast. 

![Winning_Candiate](https://user-images.githubusercontent.com/95589611/150697920-8fb0e076-ee15-47d0-bfa2-46dc64a9e12d.png)

## Election-Audit Summary: 

Though this script was used to analyze a single local, congressional election, it can and should be used to complete election audits for any election with some simple modifications. Creating an empty list and dictionary earlier in the script means that the lists and dictionaries can contain the names and values for any county or candidate. In the section of the script in which we imported our csv file containing the data for the election, one could modify this section so that their data file could be imported and read.

![modification_1](https://user-images.githubusercontent.com/95589611/150697944-0d49ea52-abf7-4570-85d4-e0dd0640ddac.png)

Once the new data is imported, all one must do is modify the for loop that iterates through the rows of the data file to refer to the approprate row that holds the candidate or county name. For example, insead of getting the candidate name from the second index (row three), you could insert the appropriate location that refers to the candidate names in your specific data file. 

![modification_2](https://user-images.githubusercontent.com/95589611/150697956-c9ea132a-066c-4e83-b44b-f387b5f6e072.png)

Once this small change is made, the script will function just as it had for our election, iterating through the rows of data to find the candidate and county names along with their vote counts. Now, the candidate and county lists and dictionaries will contain the keys and values appropriate for the new election data. This means that the second for loop in which we iterate through the dictionaries for candidate and county, will iterate through the candidates and counties for any imported dataset. Modyfing the script in these two small ways (changing the import so that it reads the new data file and setting the value of candidate and county names to their relevant rows within the data) will allow you to run this script using any election data. If your election does not use county as a variable, you can simply replace county with whatever string variable you would like to measure. 
