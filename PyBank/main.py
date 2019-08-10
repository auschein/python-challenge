#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
import csv


# In[ ]:


csv_path = os.path.join("Resources", "budget_data.csv")


# In[ ]:


date = []
profit_total = []
nmonths = 0
netpl = 0
total = 0
diff = 0


# In[ ]:


with open(csv_path, newline = "") as infile:
    reader = csv.reader(infile, delimiter = ",")
    header = next(reader)
    row1 = next(reader)
    nmonths += 1
    total += int(row1[1])
    for row in reader:
        date.append(row[0])
        diff = int(row[1]) - total
        profit_total.append(diff)
        total = int(row[1])
        nmonths += 1
        netpl = netpl + int(row[1]) 


# In[ ]:


nmonths += 1
netpl = netpl + int(row[1])
diff = int(row[1]) - total
profit_total.append(diff)
total = int(row[1])


# In[ ]:


inc = max(profit_total)
dec = min(profit_total)
profitsum = sum(profit_total)
incindex = profit_total.index(inc)
dateinc = date[incindex]
decindex = profit_total.index(dec)
datedec = date[decindex]
avgchanges =profitsum/len(profit_total)


# In[ ]:


print("Financial Analysis:")
print("------------------")
print(f" Total Months: {nmonths}")
print(f" Total: {netpl}")
print(f" Average Change: ${round(avgchanges,2)}")
print(f"Greatest Increase In Profits: {dateinc} ${incindex}")
print(f"Greatest Decrease In Profits: {datedec} ${decindex}")


# In[ ]:


#FYI...For some reason, I have to execute this block twice in order for it to produce a .txt with data in it. 
    #First execution produces a .txt file that is blank
PyBank = open("PyBank.txt", "w")

l1=("Financial Analysis:")
l2=("------------------")
l3=str(f" Total Months: {nmonths}")
l4=str(f" Total: {netpl}")
l5=str(f" Average Change: ${round(avgchanges,2)}")
l6=str(f"Greatest Increase In Profits: {dateinc} ${incindex}")
l7=str(f"Greatest Decrease In Profits: {datedec} ${decindex}")
PyBank.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(l1,l2,l3,l4,l5,l6,l7))


# In[ ]:




