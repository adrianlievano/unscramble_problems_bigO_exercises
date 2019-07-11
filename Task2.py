"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

#find unique values
unique_call_nums = []
i = 0

for i in range(len(calls)):
    if calls[i][0] not in unique_call_nums:
        unique_call_nums.append(calls[i][0])
    if calls[i][1] not in unique_call_nums:
        unique_call_nums.append(calls[i][1])
        
#build hash of unique CALL numbers and initialize to zero. O(n) runtime.
num_hash = dict()
for i in range(len(unique_call_nums)):
    num_hash[unique_call_nums[i]] = 0
    
#iterate through calls list
#If iterative element is in list of keys, increment that value to existing key's value.
j = 0

for j in range(len(calls)):
    if calls[j][0] in num_hash.keys(): #O(1)
        num_hash[calls[j][0]] += int(calls[j][3])
        
    if calls[j][1] in num_hash.keys(): #O(1)
        num_hash[calls[j][1]] += int(calls[j][3])


duration = max(num_hash.values()) #O(n)
culprit = max(num_hash, key=num_hash.get) #O(n)

print('{} spent the longest time, {} seconds, on the phone during September 2016.'.format(culprit, duration))
