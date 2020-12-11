#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Load Libraries
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


#Load Data
df = pd.read_csv('./HousingDataset.csv')
df.head()
#df.tail(10)


# In[3]:


y=df['price']


# In[4]:


x=df.drop(['ID','price'],axis=1)


# In[5]:


x.head()


# In[6]:


x_desc=x.describe()


# In[7]:


x_desc


# In[8]:


y_df=pd.DataFrame(y)


# In[9]:


y_df.describe()


# In[ ]:




