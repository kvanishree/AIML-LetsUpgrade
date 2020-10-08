#!/usr/bin/env python
# coding: utf-8

# In[12]:


with open("file1.txt","r+") as f:
    with open("file2.txt","w") as f1:
        for line in f:
            f1.write(line)


# In[ ]:




