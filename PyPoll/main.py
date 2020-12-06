import csv
import os
import statistics
csvfilepath='PyBank\\Resources\\budget_data.csv'
#PL_changes=[]
changes_average=0
PL_Change_Dic={
    "PL_Dates":[],
    "PL_Changes":[]
}
with open(csvfilepath) as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')
    header = next(csvreader)
    
    #Move to 1st row after Header
    first_row=next(csvreader)
    total_month=1
    total_PL=int(first_row[1])
    Current_row=int(first_row[1])

    #Loop through all of rows except header row
    for row in csvreader:

        #Calculate total number of months & total profit and loss
        total_month+=1
        total_PL=total_PL+int(row[1])

        #Calculate PL Changes, Add Date and PL Change to Dictionary
        PL_Change_Dic["PL_Dates"].append(row[0])
        Changes=int(row[1])-Current_row
        PL_Change_Dic["PL_Changes"].append(Changes)
        Current_row=int(row[1])

#Calculate average change
changes_average=round((sum(PL_Change_Dic["PL_Changes"])/len(PL_Change_Dic["PL_Changes"])),2)
Greatest_Increase=int(PL_Change_Dic["PL_Changes"][0])
Greatest_Decrease=int(PL_Change_Dic["PL_Changes"][0])

#Find Greatest increase and decrease
for i in range(1,len(PL_Change_Dic["PL_Changes"])-1):
    if int(PL_Change_Dic["PL_Changes"][i])>Greatest_Increase:
        Greatest_Increase=int(PL_Change_Dic["PL_Changes"][i])
        Increase_date=PL_Change_Dic["PL_Dates"][i]
        Greatest_Increase=int(PL_Change_Dic["PL_Changes"][i])
    elif int(PL_Change_Dic["PL_Changes"][i])<Greatest_Decrease:
        Greatest_Decrease=PL_Change_Dic["PL_Changes"][i]
        Decrease_date=PL_Change_Dic["PL_Dates"][i]    

#Print result on terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total Month: {total_month}")
print(f"Total: ${total_PL}")
print(f"Average Change: ${changes_average}")
print(f"Greatest Increase in Profits: {Increase_date} (${Greatest_Increase})")
print(f"Greatest Decrease in Profits: {Decrease_date} (${Greatest_Decrease})")

#Send result to TXT file
txtfilepath='PyBank\\Analysis\\output.txt'
with open(txtfilepath, "w") as txt_file:
    txt_file.write("Financial Analysis")
    txt_file.write("\n")
    txt_file.write("----------------------------")
    txt_file.write("\n")
    txt_file.write(f"Total Month: {total_month}")
    txt_file.write("\n")
    txt_file.write(f"Total: ${total_PL}")
    txt_file.write("\n")
    txt_file.write(f"Average Change: ${changes_average}")
    txt_file.write("\n")
    txt_file.write(f"Greatest Increase in Profits: {Increase_date} (${Greatest_Increase})")
    txt_file.write("\n")
    txt_file.write(f"Greatest Decrease in Profits: {Decrease_date} (${Greatest_Decrease})")
    