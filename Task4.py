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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

#check calls database
#gets only callers
unique_num_callers = []
i = 0
j = 0

for i in range(len(calls)):
    if calls[i][0] not in unique_num_callers:
        unique_num_callers.append(calls[i][0])

sender_texts = []

for j in range(len(texts)):
        if texts[j][0] not in sender_texts:
            sender_texts.append(texts[j][0])

sorted(sender_texts)
sorted(unique_num_callers)

for ele in sender_texts:
    if ele in unique_num_callers:
        unique_num_callers.remove(ele)

tele_nums = sorted(unique_num_callers)

print("These numbers may be telemarkers: ")
for i in tele_nums:
    print('{}'.format(i))
