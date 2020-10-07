#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[16]:


import numpy as np


# In[158]:


df = pd.read_excel('Номенклатура.xlsx')


# In[10]:


mang = pd.read_excel('табл по деп.xlsx')


# In[104]:


pd.set_option('display.max_columns', None)


# In[159]:


df = df.iloc[3:]
df.columns = df.iloc[0]


# In[161]:


df = df.iloc[1:]


# In[171]:


df1 = pd.merge(df,
               mang,
               on ='Редакция',  
               how ='inner')


# In[172]:


df1['Дата посл.тиража'] = df1['Дата посл.тиража'].astype(str)


# In[173]:


df1 = df1[df1['Дата посл.тиража'] > '2018-01-09']


# In[174]:


df1.columns = ['ВСЕ_2019 ' + i if ((ix > 11) & (ix < 24)) else i for ix, i in enumerate(df1.columns)]


# In[176]:


df1.columns = ['ВСЕ_2020 ' + i if ((ix > 23) & (ix < 36)) else i for ix, i in enumerate(df1.columns)]


# In[178]:


df1.columns = ['РЫНОК_2019 ' + i if ((ix > 35) & (ix < 48)) else i for ix, i in enumerate(df1.columns)]


# In[180]:


df1.columns = ['РЫНОК_2020 ' + i if ((ix > 47) & (ix < 60)) else i for ix, i in enumerate(df1.columns)]


# In[182]:


df1.columns = ['ЛАБИРИНТ_2019 ' + i if ((ix > 59) & (ix < 72)) else i for ix, i in enumerate(df1.columns)]


# In[183]:


df1.columns = ['ЛАБИРИНТ_2020 ' + i if ((ix > 71) & (ix < 84)) else i for ix, i in enumerate(df1.columns)]


# In[185]:


df1.columns = ['OZON_2019 ' + i if ((ix > 83) & (ix < 96)) else i for ix, i in enumerate(df1.columns)]


# In[186]:


df1.columns = ['OZON_2020 ' + i if ((ix > 95) & (ix < 108)) else i for ix, i in enumerate(df1.columns)]


# In[188]:


df1.columns = ['WB_2019 ' + i if ((ix > 107) & (ix < 120)) else i for ix, i in enumerate(df1.columns)]


# In[189]:


df1.columns = ['WB_2020 ' + i if ((ix > 119) & (ix < 132)) else i for ix, i in enumerate(df1.columns)]


# In[191]:


df1.columns = ['ЧГ_2019 ' + i if ((ix > 131) & (ix < 144)) else i for ix, i in enumerate(df1.columns)]


# In[192]:


df1.columns = ['ЧГ_2020 ' + i if ((ix > 143) & (ix < 156)) else i for ix, i in enumerate(df1.columns)]


# In[201]:


all_2019 = df1.columns.str.startswith('ВСЕ_2019')
df1['ВСЕ_2019'] = df1.iloc[:,all_2019].sum(axis=1)


# In[203]:


all_2020 = df1.columns.str.startswith('ВСЕ_2020')
df1['ВСЕ_2020'] = df1.iloc[:,all_2020].sum(axis=1)


# In[205]:


mark_2019 = df1.columns.str.startswith('РЫНОК_2019')
df1['РЫНОК_2019'] = df1.iloc[:,mark_2019].sum(axis=1)


# In[206]:


mark_2020 = df1.columns.str.startswith('РЫНОК_2020')
df1['РЫНОК_2020'] = df1.iloc[:,mark_2020].sum(axis=1)


# In[208]:


lab_2019 = df1.columns.str.startswith('ЛАБИРИНТ_2019')
df1['ЛАБИРИНТ_2019'] = df1.iloc[:,lab_2019].sum(axis=1)


# In[209]:


lab_2020 = df1.columns.str.startswith('ЛАБИРИНТ_2020')
df1['ЛАБИРИНТ_2020'] = df1.iloc[:,lab_2020].sum(axis=1)


# In[211]:


ozon_2019 = df1.columns.str.startswith('ОЗОН_2019')
df1['ОЗОН_2019'] = df1.iloc[:,ozon_2019].sum(axis=1)


# In[212]:


ozon_2020 = df1.columns.str.startswith('ОЗОН_2020')
df1['ОЗОН_2020'] = df1.iloc[:,ozon_2020].sum(axis=1)


# In[214]:


wb_2019 = df1.columns.str.startswith('WB_2019')
df1['WB_2019'] = df1.iloc[:,wb_2019].sum(axis=1)


# In[215]:


wb_2020 = df1.columns.str.startswith('WB_2020')
df1['WB_2020'] = df1.iloc[:,wb_2020].sum(axis=1)


# In[219]:


ch_2019 = df1.columns.str.startswith('ЧГ_2019')
df1['ЧГ_2019'] = df1.iloc[:,ch_2019].sum(axis=1)


# In[217]:


ch_2020 = df1.columns.str.startswith('ЧГ_2020')
df1['ЧГ_2020'] = df1.iloc[:,ch_2020].sum(axis=1)


# In[221]:


df1.to_excel('Данные по книгам.xlsx')

