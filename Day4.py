#!/usr/bin/env python
# coding: utf-8

# In[8]:


#Q1
print("enter the operation to perform")
a=input()
if(a=='+'):
    c=(3+2j)+(5+4j)
    print(c)
elif(a=='-'):
    c=(3+2j)-(5+4j)
    print(c)
elif(a=='*'):
    c=(3+2j)*(5+4j)
    print(c)
elif(a=='/'):
    c=(3+2j)/(5+4j)
    print(c)
elif(a=='//'):
    print("floor division of two number is not possible\n")
elif(a=='%'):
    print("module is not possible to do in complex numbers\n")
else:
    print("enter correct operation")


# #Q2
# range()
# range(start,stop,step)
#     start:it is not compulsory but if we want we can mention this for where to start..
#     stop:it is required and compulsory to mention , this for where to stop..
#     step: it is not compulsory to mention , but if we requird to print one step forward number of every number.. 
#  

# In[21]:


#ex 
for i in range(5):
    print(i)
print("---------------")
list=[1,2,3,4,5,6,7]
for list in range(1,5,2):
    print(list)


# In[23]:


#Q3
a=int(input(print("enter the num1\n")))
b=int(input(print("enter the num1\n")))
c=a-b
if(c>25):
    print("multiplication is = ",a*b)
else:
    print("division is = ",a/b)


# In[2]:


#Q4
l=[1,2,3,4,5,6]
for i in range(len(l)):
    if(l[i]%2==0):
        print("square of the number minus 2\n")


# In[3]:


#Q5
l2=[12,14,16,17,8]
for i in range(len(l2)):
    if (l2[i]/2)>7:
        print(l2[i],end=" ")


# In[ ]:




