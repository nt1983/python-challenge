import csv
import os

csvfilepath='PyPoll\\Resources\\election_data.csv'

Candidates_Dic={
    "Name":[],
    "Vote_percent":[],
    "Candidate_Votes":[]
}
with open(csvfilepath) as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')
    header=next(csvreader)
    
    #Move to 1st row after Header
    first_row=next(csvreader)
    Total_votes=1
    Candidates_Dic["Name"].append(first_row[2])
    Candidates_Dic["Candidate_Votes"].append(1)
    
    for row in csvreader:
        Total_votes+=1
        #Find Candidate name and total of votes per candidate
        if row[2] not in Candidates_Dic["Name"]:
            Candidates_Dic["Name"].append(row[2])
            Candidates_Dic["Candidate_Votes"].append(1)
        else:
            index=Candidates_Dic["Name"].index(row[2])
            Candidates_Dic["Candidate_Votes"][index]+=1

Winner=Candidates_Dic["Candidate_Votes"][0]
Winner_name=Candidates_Dic["Name"][0]
#Calculate percentage and find winner
for i in range(len(Candidates_Dic["Name"])):
    Candidates_Dic["Vote_percent"].append(round(Candidates_Dic["Candidate_Votes"][i]/Total_votes*100,3))
    if Winner < Candidates_Dic["Candidate_Votes"][i]:
        Winner=Candidates_Dic["Candidate_Votes"][i]
        Winner_name=Candidates_Dic["Name"][i]

#Print result on terminal
print("Election Results")
print("----------------------------")
print(f"Total Votes: {Total_votes}")
print("----------------------------")
for i in range(len(Candidates_Dic["Name"])):
    vote=Candidates_Dic["Vote_percent"][i]
    print(str(Candidates_Dic["Name"][i])+": "+f"{vote:.3f}% ("+str(Candidates_Dic["Candidate_Votes"][i])+")")
print("----------------------------")
print(f"Winner: {Winner_name}")

#Send result to TXT file
txtfilepath='PyPoll\\Analysis\\output.txt'
with open(txtfilepath, "w") as txt_file:
    txt_file.write("Election Results")
    txt_file.write("\n")
    txt_file.write("----------------------------")
    txt_file.write("\n")
    txt_file.write(f"Total Votes: ${Total_votes}")
    txt_file.write("\n")
    txt_file.write("----------------------------")
    txt_file.write("\n")
    for i in range(len(Candidates_Dic["Name"])):
        vote=Candidates_Dic["Vote_percent"][i]
        txt_file.write(str(Candidates_Dic["Name"][i])+": "+f"{vote:.3f}% ("+str(Candidates_Dic["Candidate_Votes"][i])+")")
        txt_file.write("\n")
    txt_file.write("----------------------------")
    txt_file.write("\n")
    txt_file.write(f"Winner: {Winner_name}")