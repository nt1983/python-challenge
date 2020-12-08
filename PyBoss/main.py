import csv
import os
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}
csvfilepath='PyBoss\\Resources\\employee_data.csv'
Formated_Dic={
    "Emp ID":[],
    "First Name":[],
    "Last Name":[],
    "DOB":[],
    "SSN":[],
    "State":[]
}
with open(csvfilepath) as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')
    header=next(csvreader)

    for row in csvreader:
        #Add proper value of Emp ID data dictionary
        Formated_Dic["Emp ID"].append(row[0])
        #split first name & last name, add them separatly to data dictionary
        fullname=row[1].split(" ")
        Formated_Dic["First Name"].append(fullname[0])
        Formated_Dic["Last Name"].append(fullname[1])
        #Split Date and change Date format to mm/dd/yyyy
        dob=row[2].split("-")
        Formated_Dic["DOB"].append(dob[1]+"/"+dob[2]+"/"+dob[0])
        #Split SSN by - and change format to ***-**-xxxx, add to Data dictionary
        ssn=row[3].split("-")
        Formated_Dic["SSN"].append("***-**-"+ssn[2])
        #Find State abbreviation, add to data dictionary
        Formated_Dic["State"].append(us_state_abbrev[row[4]])

#create new csv file
formattedfile='PyBoss\\Resources\\formatted_csv.csv'
with open(formattedfile, 'w', newline='') as formatted_csv:
    csvwriter=csv.writer(formatted_csv,delimiter=',')
    
    #Add header first and then data rows
    csvwriter.writerow(['Emp ID','First Name','Last Name','DOB', 'SSN','State'])
    for i in range(len(Formated_Dic["Emp ID"])):
        csvwriter.writerow([Formated_Dic["Emp ID"][i],Formated_Dic["First Name"][i],Formated_Dic["Last Name"][i],Formated_Dic["DOB"][i], Formated_Dic["SSN"][i],Formated_Dic["State"][i]])
    

