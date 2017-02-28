
# coding: utf-8

# In[ ]:

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas import DataFrame
get_ipython().magic('matplotlib inline')


# In[140]:

names_by_year = {}
for year in range(1900, 2001):
    names_by_year[year] = pd.read_csv(
        '/Users/Anton/Desktop/python/net/17/names/yob{}.txt'.format(year),
        names=['Name', 'Gender', 'Count'])
names_all = pd.concat(names_by_year, names=['Year', 'Pos'])


# In[141]:

names_all


# In[142]:

name_dynamics = names_all.groupby([names_all.index.get_level_values(0), 'Name']).sum()
name_dynamics.head(10)


# In[143]:

name_dynamics.query('Name == ["Ruth", "Robert"]').unstack('Name').plot()


# In[144]:

names_by_year = {}
for year in range(1900, 2005, 5):
    names_by_year[year] = pd.read_csv(
        '/Users/Anton/Desktop/python/net/17/names/yob{}.txt'.format(year),
        names=['Name', 'Gender', 'Count'])
names_all = pd.concat(names_by_year, names=['Year', 'Pos'])


# In[145]:

name_dynamics = names_all.groupby([names_all.index.get_level_values(0), 'Name']).sum()
name_dynamics.query('Name == ["Ruth", "Robert"]').unstack('Name').plot.bar()


# In[146]:

names_by_year = pd.read_csv('/Users/Anton/Desktop/python/net/17/names/yob1950.txt', names=['Name', 'Gender', 'Count'])


# In[147]:

name_r = []
for nam in names_with_r['Name']:
    if('R' in nam):
        name_r.append(nam)
arr_with_r_in_name = names_by_year.query('Name in {}'.format(name_r))
#arr_with_r_in_name
arr_with_r_in_name.groupby('Name').sum().sort_values(by='Count', ascending=False).plot.pie(y='Count')


# In[148]:

#names_with_r = names_by_year.apply(lambda row:[row.Name, row.Gender, row.Count], axis=1)


# In[149]:

names_by_year = {}
for year in range(1900, 2001):
    names_by_year[year] = pd.read_csv(
        '/Users/Anton/Desktop/python/net/17/names/yob{}.txt'.format(year),
        names=['Name', 'Gender', 'Count'])
names_all = pd.concat(names_by_year, names=['Year', 'Pos'])


# In[150]:

names_all


# In[242]:

import json
from collections import Counter


symbols = []
arr_numb = []
arr_symb = []
count_symbols = {}

for i in names_all['Name']:
    for s in i:
        symbols.append(s.lower())
        
c = Counter(symbols)
z = c.most_common()

for v in z:
    arr_numb.append(v[1])
    arr_symb.append(v[0])

count_symbols['Symbol'] = arr_symb
count_symbols['Number'] = arr_numb

count_symbols


# In[241]:

df = DataFrame(data=count_symbols)
df


# In[240]:

df.plot.scatter(x='Symbol', y='Number')
