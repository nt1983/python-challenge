import csv
import os
import statistics
filepath='Resources\\budget_data.csv'
#PL_changes=[]
changes_average=0
PL_Change_Dic={
    "PL_Dates":[],
    "PL_Changes":[]
}
with open(filepath) as csvfile:
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

changes_average=statistics.mean(PL_Change_Dic["PL_Changes"])
Greatest_Increase=max(PL_Change_Dic["PL_Changes"])
Greatest_Decrease=min(PL_Change_Dic["PL_Changes"])

for i in range(len(PL_Change_Dic["PL_Changes"])-1):
    if int(PL_Change_Dic["PL_Changes"][i])==Greatest_Increase:
        Increase_date=PL_Change_Dic["PL_Dates"][i]
    elif int(PL_Change_Dic["PL_Changes"][i])==Greatest_Decrease:
        Decrease_date=PL_Change_Dic["PL_Dates"][i]    


print(total_month, total_PL,changes_average, Greatest_Increase, Increase_date, Greatest_Decrease, Decrease_date)
