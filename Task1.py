"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

unique_num = []
i = 0
#check text database

#check sending nums
for i in range(len(texts)):
    if texts[i][0] not in unique_num:
        unique_num.append(texts[i][0])
        
    if texts[i][1] not in unique_num:
        unique_num.append(texts[i][1])
        
#check calls database
for i in range(len(calls)):
    if calls[i][0] not in unique_num:
        unique_num.append(calls[i][0])
        
    if calls[i][1] not in unique_num:
        unique_num.append(calls[i][1])
        
print("There are {} different telephone numbers in the records".format(len(unique_num)))
