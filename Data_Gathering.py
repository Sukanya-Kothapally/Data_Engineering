#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')

from urllib.request import urlopen
from bs4 import BeautifulSoup


# In[4]:


url = "http://www.hubertiming.com/results/2017GPTR10K"
html = urlopen(url)
soup = BeautifulSoup(html, 'lxml')
type(soup)


# In[5]:


title=soup.title
print(title)


# In[6]:


text=soup.get_text()
print(soup.text)


# In[14]:


all_links=soup.find_all('a')
for link in all_links:
    print(link.get("href"))


# In[ ]:


soup.find_all('table')


# In[ ]:


soup.find_all('tr')


# In[ ]:


soup.find_all('th')


# In[ ]:


soup.find_all('td')


# In[8]:


rows=soup.find_all('tr')
print(rows[:10])


# In[9]:


for row in rows:
    row_td=row.find_all('td')
print(row_td)
type(row_td) 


# In[10]:


str_cells=str(row_td)
cleantext=BeautifulSoup(str_cells,"lxml").get_text()
print(cleantext)


# In[11]:


import re

list_rows=[]
for row in rows:
    cells=row.find_all('td')
    str_cells=str(cells)
    clean1=re.compile('<.*?>')
    clean2=re.sub(clean1,'',str_cells)
    list_rows.append(clean2)
print(clean2)
type(clean2) 


# In[12]:


df=pd.DataFrame(list_rows)
df.head(10)


# In[13]:


df1=df[0].str.split(',',expand=True)
df1.head(10)


# In[14]:


df1[0]=df1[0].str.strip('[')
df1.head(10)


# In[15]:


col_labels=soup.find_all('th')
all_headers=[]
col_str=str(col_labels)
cleantext2=BeautifulSoup(col_str,"lxml").get_text()
all_headers.append(cleantext2)
print(all_headers)


# In[18]:


df2=pd.DataFrame(all_headers)
df2.head()


# In[19]:


df3=df2[0].str.split(',',expand=True)
df3.head()


# In[20]:


frames=[df3,df1]
df4=pd.concat(frames)
df4.head(10)


# In[21]:


df5=df4.rename(columns=df4.iloc[0])
df5.head()


# In[22]:


df5.info()


# In[23]:


df5.shape


# In[24]:


df6=df5.dropna(axis=0,how='any')
df6.info()


# In[25]:


df6.shape


# In[26]:


df7=df6.drop(df6.index[0])
df7.head()


# In[27]:


df7.rename(columns={'[Place':'Place'},inplace=True)
df7.rename(columns={' Team]':'Team'},inplace=True)
df7.head()


# In[28]:


df7['Team']=df7['Team'].str.strip(']')
df7.head()


# In[46]:


# As the State is redudant removing it *** Extra ***
df7.drop([' State'], axis = 1) 


# In[71]:


time_list = df7[' Chip Time'].tolist()
time_mins = []
for time in time_list:
    total_time_list=time.split(':')
    #print(total_time_list)
    if(len(total_time_list) == 3):
        h = total_time_list[0]
        m = total_time_list[1]
        s = total_time_list[2]
    else:
        h = 0
        m = total_time_list[0]
        s = total_time_list[0]
    math = (int(h) * 3600 + int(m) * 60 + int(s))/60
    time_mins.append(math)
print(time_mins)  


# In[72]:


df7['Runner_mins'] = time_mins
df7.head()


# In[73]:


df7.describe(include=[np.number])


# In[75]:


from pylab import rcParams
rcParams['figure.figsize'] = 15,5

df7.boxplot(column="Runner_mins")
plt.grid(True, axis='y')
plt.ylabel('CHIP TIME')
plt.xticks([1],['Runners'])


# In[80]:


x= df7['Runner_mins']
ax=sns.distplot(x,hist=True,kde=True,rug=False,color='m',bins=25,hist_kws={'edgecolor':'black'})
plt.show()


# In[96]:


fem = df7.loc[df7[' Gender']==' F']['Runner_mins']
mal = df7.loc[df7[' Gender']==' M']['Runner_mins']
sns.distplot(fem, hist=True, kde=True, rug=False, hist_kws={'edgecolor':'black'}, label='Female')
sns.distplot(mal, hist=False, kde=True, rug=False, hist_kws={'edgecolor':'black'}, label='Male')
plt.legend()


# In[97]:


group_stats = df7.groupby(" Gender", as_index=True).describe()
print(group_stats)


# In[98]:


df7.boxplot(column='Runner_mins',by=' Gender')
plt.ylabel('Chip Time')
plt.suptitle("")

