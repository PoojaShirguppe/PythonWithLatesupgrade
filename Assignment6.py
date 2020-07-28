#!/usr/bin/env python
# coding: utf-8

# # convert list to dictionary in one line code using comprehension (without using zip)

# In[2]:


"""
list1 = [1,2,3,4,5,7,8]
list2 = ['a','b','c','d','e']
d1 = {list1[each]:list2[each] for each in range(min(len(list1),len(list2)))}
print(d1)
"""


# In[5]:


list1= [1,2,3,4,5,6,7,8]
list2= ['a','b','c','d','e']
result = {}
for key in list1:
    for values in list2:
        result[key] = values
        list2.remove(values)
        break
print(str(result))


# In[ ]:




