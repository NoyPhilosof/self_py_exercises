#!/usr/bin/env python
# coding: utf-8

# In[3]:


get_ipython().system('pip install pandas')


# In[2]:


from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())


# In[25]:


e.get_attribute("href")


# In[28]:


h = None

for e in driver.find_elements_by_id("video-title"):
    h = e.get_attribute("href")
    if h:
        break
driver.get(h)


# In[19]:


e = e[0]


# In[23]:





# In[12]:


for e in driver.find_elements_by_id("contents"):
    ne = e.find_elements_by_par


# In[11]:


es

