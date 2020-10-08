#!/usr/bin/env python
# coding: utf-8

# In[6]:


start=0
end=100
for i in range(start,end):
    if i>1:
        for j in range(2,i):
            
            if(i%j==0):
                break
        else:
            if(i%2!=0):
                print(i)
                
            
                


# In[34]:


s="vani"
s1="i am studying"
print(s.capitalize())

print(s.casefold())
print(s.isalpha())
print(s.isalnum())
print(s.islower())
print(s.isspace())
print(s.istitle())
print(s.lower())
print(s.split(maxsplit=-2))
print(s1.istitle())
print(s1.isupper())
print(s1+s)
print(s[::-1])


# In[39]:


string=input("enter the string to check palindrome or not \n ")
s2=string[::-1]
if(s2==string):
    print("its palindrome\n")
print("NO,its not a palindrome\n")


# In[53]:


s4=input("enter the string\n")
i=s4.lower().replace("@","").replace(" ","")
print(i)

