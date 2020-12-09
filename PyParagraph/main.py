import os
import re

txtfilepath='PyParagraph\\raw_data\\paragraph_2.txt'
letter=0

#Open and read txt file
with open(txtfilepath,"r", encoding="utf8") as txtfile:
    txt=txtfile.read()

#calculate count of word, count of sentence and count of letters
word_count=len(txt.split(' '))
sentence=re.split('[.!?”]', txt)
while sentence.count('')>0:
    sentence.remove('')
sentence_count=len(sentence)
i=0
for i in txt:
    if i.isalpha():
        letter+=1

#Calculate average number of letters and average sentence length
letter_avg=round(letter/word_count,2)
sentence_avg=round(word_count/sentence_count,2)  

#Print results on terminal
print("\n")
print("Paragraph Analysis")
print("-----------------")
print(f"Approximate Word Count: {word_count}")
print(f"Approximate Sentence Count: {sentence_count}")
print(f"Average Letter Count: {letter_avg}")
print(f"Average Sentence Length: {sentence_avg}")

#Write results in txt file.
txtfilepath='PyParagraph\\Paragraph_Analyze.txt'
with open(txtfilepath, "w") as txt_file:
    txt_file.write("Paragraph Analysis")
    txt_file.write("\n")
    txt_file.write("-----------------")
    txt_file.write("\n")
    txt_file.write(f"Approximate Word Count: {word_count}")
    txt_file.write("\n")
    txt_file.write(f"Approximate Sentence Count: {sentence_count}")
    txt_file.write("\n")
    txt_file.write(f"Average Letter Count: {letter_avg}")
    txt_file.write("\n")
    txt_file.write(f"Average Sentence Length: {sentence_avg}")
 