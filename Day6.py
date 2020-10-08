#!/usr/bin/env python
# coding: utf-8

# In[11]:


n=input("enter the Gmail\n")
f=n.rfind("@")
#print(f)
l=n.rfind(".")
#print(l)
print(n[f+1:l])


# In[23]:


n=("without","hello","bag","world")
x=sorted(n)
print(x)

    Sets-A set is a collection which is unordered and    unindexed. In Python, sets are written with curly brackets
    ->cannot be sure in which order the items will appear
    ->You cannot access items in a set by referring to an index or a key  but can loop
    example-
            set={'a','b',1,2,3,4}
            output:
                {1, 2, 3, 4, 'a', 'b'}
# In[1]:


a=input("enter the numbers\n")
x=a.replace(" ","")
print(type(x))
i=1
j=0
#h=len(x)
#print(h)

while (int(x[j])!=i):
    print(x[j])
    j=j+1
    i=i+1
    if(j>len(x)):
        break


# In[8]:


l=[1,2,3,4,5,3,2,1]
print(set(l))

