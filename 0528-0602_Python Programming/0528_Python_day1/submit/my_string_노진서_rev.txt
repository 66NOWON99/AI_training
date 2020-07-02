#!/usr/bin/env python
# coding: utf-8

# In[1]:


#replace(a,b)


# In[6]:


str="this is a string"
a='is'
b='IS'


# In[36]:


if(str.count(a)==0):
    print(str)
else:
    for i in range(str.count(a)):
        tmp=str
        tmp=str[0:str.find(a)]+b+str[str.find(a)+len(a):len(str)]
        str=tmp
print(str)


# In[41]:


#str.find(a)

if a not in str:
    return -1
else: # a is in str
    for i in range(len(str)):
        if(str[i]==a):
            return i
        


# In[42]:


#str.startswith(a)
if len(str)>0:
    if str[0]==a:
        return True
    else:
        return False


# In[44]:


#str.endswith(a)
if len(str)>0:
    if str[len(str)-1]==a:
        return True
    else:
        return False


# In[45]:


str="this is a string "
lst=[]
for c in str:
    lst.append(c)
# print(lst)

if len(lst)>0:
    t=lst[0].upper()
    lst[0]=t
    
    for i in range(1,len(str)):
        if(lst[i-1]==" "):
            m=lst[i].upper()
            lst[i]=m

print(lst)
ans=""
for i in range(len(lst)):
    ans=ans+lst[i]

