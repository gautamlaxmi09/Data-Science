#!/usr/bin/env python
# coding: utf-8

# In[1]:


import itertools
from itertools import product
box_1=['g','b']
perm=[]
for p in itertools.product(box_1, repeat=2):
    perm.append(p)
perm


# In[2]:


box_2=['g','b','y']
perm=[]
for p in itertools.product(box_2, repeat=3):
    perm.append(p)
perm


# In[3]:


import itertools

box_1=['g','b']
perm=itertools.permutations(box_1)
for i in list(perm):
    print(i)


# In[4]:


box_2 =['g','b','y']
perm=itertools.permutations(box_2)
for i in list(perm):
    print(i)


# In[5]:


box_2=['g','b','y']
perm=[]
for p in itertools.product(box_2,repeat=2):
    perm.append(p)
perm


# In[6]:


box_2=['g','b','y']
perm=itertools.permutations(box_2,2)
for i in list(perm):
    print(i)


# In[7]:


from itertools import combinations_with_replacement
box_1=['g','b']
comb=combinations_with_replacement(box_1,2)
for i in list(comb):
    print(i)


# In[8]:


from itertools import combinations_with_replacement
box_2=['g','b','y']
comb=combinations_with_replacement(box_2,2)
for i in list(comb):
    print(i)


# In[9]:


from itertools import combinations
comb=combinations(box_1,2)
for i in list(comb):
    print(i)


# In[10]:


from itertools import combinations
comb=combinations(box_2,2)
for i in list(comb):
    print(i)


# In[ ]:




