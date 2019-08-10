#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
import csv


# In[ ]:


csvpath = os.path.join("Resources", "election_data.csv")


# In[ ]:


tvotes = 0
nvotes = []
pvotes = []
candidate = []


# In[ ]:


with open (csvpath, newline = "") as infile:
    reader = csv.reader(infile, delimiter = ",")
    header = next(reader)
    for i in reader:
        tvotes += 1
        if i[2] not in candidate:
            candidate.append(i[2])
            index = candidate.index(i[2])
            nvotes.append(1)
        else:
            index = candidate.index(i[2])
            nvotes[index] += 1


# In[ ]:


for votes in nvotes:
    perc = (votes/tvotes)*100
    perc = round(perc)
    pvotes.append(perc)


# In[ ]:


win = max(nvotes)
index = nvotes.index(win)
wincand = candidate[index]


# In[ ]:


print ('Election Results')
print ('----------------')
print (f'Total Votes Counted: {str(tvotes)}')
print ('----------------')
for x in range(len(candidate)):
    print (f'{str(candidate[x])} got: {str(pvotes[x])}% of the vote and ({str(nvotes[x])}) of the votes counted')
print ('----------------')
print (f'The Winning Candidate is: {wincand}')


# In[ ]:


#FYI...For some reason, I have to execute this command twice for it to produce a .txt with data in it. 
    #First execution produces a .txt file that is blank
PyPoll = open("PyPoll.txt", "w")

l1=("Election Results:")
l2=("------------------")
l3=str(f'Total Votes Counted: {str(tvotes)}')
l4=str('----------------')
PyPoll.write('{}\n{}\n{}\n{}\n'.format(l1,l2,l3,l4))
for x in range(len(candidate)):
    results = (f'{str(candidate[x])} got: {str(pvotes[x])}% of the vote and ({str(nvotes[x])}) of the votes counted')
    PyPoll.write('{}\n'.format(results))
l5=('----------------')
l6=str(f'The Winning Candidate is: {wincand}')
PyPoll.write('{}\n{}\n'.format(l5,l6))


# In[ ]:





# In[ ]:




