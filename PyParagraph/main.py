import os
import re

txtfilepath='PyParagraph\\raw_data\\test.txt'
ormated_Dic={
    "Emp ID":[],
    "First Name":[],
    "Last Name":[],
    "DOB":[],
    "SSN":[],
    "State":[]
}
txt=" "
re.split("(?<=[.!?]) +", txt)
with open(txtfilepath,"r", encoding="utf8") as txtfile:
    txt=txtfile.read()
    re.split("(?<=[.!?]) +", txt)
    word_count=len(txt.split(' '))
    


print(word_count)