#!/usr/bin/env python
# coding: utf-8

# In[26]:


import pandas as pd
import numpy as np
import math

pd.options.display.max_columns = None
pd.options.display.max_rows = None
df = pd.read_csv ('CrashData_2019.csv')

float_columns = df.select_dtypes(include=['float64'])
float_columns_list = list(float_columns.columns.values)
for i in float_columns_list:
    df[i] = df[i].astype('Int64')
    #print(df.dtypes)
    first5 = df.head()
    print(first5)


# In[5]:


#Reitreated Assertions After B

# Existence Assertion 1: Each record should not be NULl
count=0
for i, row in df.iterrows():
    records=row['Record Type']
    if(math.isnan(records)):
        df.drop(df.index[i])
        count+=1
if(count==0):
    print("The records are not null")


# In[6]:


# Existence Assertion 2: Check if any record has NULL crash ID
count=0
for i, row in df.iterrows():
    records=row['Crash ID']
    if(math.isnan(records)):
        df.drop(df.index[i])
        count+=1
if(count==0):
    print("The records are not null")


# In[ ]:


# Limit Assertion 1: for all records each record's crash hour should
# be greater than 0 and less than 24, 99 if time is not given 
count=0
count1=0
for i, row in df.iterrows():
    crash_hr=row['Crash Hour']
    print(crash_hr)
    if(crash_hr>=0 and crash_hr<=23):
        count+=1
        if(crash_hr==99):
            count1+=1
        else:
            pass
    else:
        pass
print("records which have 0 and 24 are",count)
print("records which dont have time are",count1)          
            


# In[23]:


# For all records which have recordtype=3 should have both Vehicle ID and Participant ID not null.
count=0
for i, row in df.iterrows():
    three=row['Record Type']
    if(three == 3):
        part=row['Participant ID']
        vehi=row['Vehicle ID']
        if(math.isnan(part) and math.isnan(vehi)):
            df.drop(df.index[i])
            count+=1
if(count==0):
    print("records which have record type as 3 have both vehicle and participant id")


# In[24]:


# For all records which have recordtype=2 should have Vehicle ID.
count=0
for i, row in df.iterrows():
    two=row['Record Type']
    if(two == 2):
        vehi=row['Vehicle ID']
        if( math.isnan(vehi)):
            df.drop(df.index[i])
            count+=1
if(count==0):
    print("records which have record type as 2 have vehicle")


# In[25]:


# For all records which have recordtype=1 should have serial #.
count=0
for i, row in df.iterrows():
    one=row['Record Type']
    if(one == 1):
        vehi=row['Serial #']
        if( math.isnan(vehi)):
            df.drop(df.index[i])
            count+=1
if(count==0):
    print("records which have record type as 1 have serial #")


# In[ ]:




