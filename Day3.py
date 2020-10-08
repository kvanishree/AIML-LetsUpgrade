#!/usr/bin/env python
# coding: utf-8

# In[2]:


#to subtract two complex numbers
a=1000
b=500
a-b


# In[4]:


#find fourth root
a=6
b=a**0.25
b


# In[7]:


#swap using temp
a=10
b=20
temp=a
a=b
b=temp
print("a=",a,"b=",b)


# In[12]:


#swap without temp
a=60
b=80
a=a+b
b=a-b
a=a-b
print("a=",a)
print("b=",b)


# In[16]:


#Fahrentheit to kelvin and celsius
print("enter the value in Fahrenheit\n")
a=37
b=(a-32)*(5/9)+273.15
print("kelvin =",b)
c=(a-32)*(5/9)
print("celsius =",c)


# In[33]:


#DataTypes
a=10
print(type(a))
b=10.111
print(type(b))
c=[1,'vani',10.12]
print(type(c))
d=(2,'yash',1.23)
print(type(d))
e='vani'
print(type(e))
f={"g":"10","h":"hii"}
print(type(f))
g={1,"vani"}
print(type(g))


# In[ ]:




