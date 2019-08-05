#!/usr/bin/env python
# coding: utf-8

# In[27]:


import os
import csv


# In[28]:


csvpath = os.path.join("..", "Resources", "election_data.csv")
csvpath


# In[29]:


tvotes = 0
nvotes = []
pvotes = []
candidate = []


# In[77]:


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


# In[88]:


for votes in nvotes:
    perc = round(votes/tvotes)*100
    'perc = "%.3f%%" % perc
    pvotes.append(perc)


# In[81]:


win = max(nvotes)
index = nvotes.index(win)
wincand = candidate[index]


# In[87]:


print ('Election Results')
print ('----------------')
print (f'Total Votes Counted: {str(tvotes)}')
print ('----------------')
for x in range(len(candidate)):
    print (f'{str(candidate[x])} got: {str(pvotes[x])} of the vote and ({str(nvotes[x])}) of the votes counted')
print ('----------------')
print (f'The Winning Candidate is: {wincand}')


# In[ ]:




